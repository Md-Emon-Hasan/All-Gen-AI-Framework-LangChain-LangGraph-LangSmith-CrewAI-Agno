"""Coordinate specialist web-search and financial agents with Agno Team."""

import os

from agno.agent import Agent
from agno.models.google import Gemini
from agno.models.groq import Groq
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

gemini_model = Gemini(id=os.getenv("GEMINI_MODEL", "gemini-3.7-flash"))
web_model = (
    Groq(id=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"))
    if os.getenv("GROQ_API_KEY")
    else gemini_model
)

web_agent = Agent(
    name="Web Researcher",
    role="Find relevant information on the web and summarize it with sources.",
    model=web_model,
    tools=[DuckDuckGoTools()],
    markdown=True,
)

finance_agent = Agent(
    name="Financial Analyst",
    role="Retrieve and explain company and stock information.",
    model=gemini_model,
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_info=True,
            company_news=True,
        )
    ],
    markdown=True,
)

research_team = Team(
    name="Financial Research Team",
    model=gemini_model,
    members=[web_agent, finance_agent],
    instructions=[
        "Delegate current web research to the Web Researcher and market data questions to the Financial Analyst.",
        "Combine the findings into a concise report and distinguish sourced facts from analysis.",
    ],
    markdown=True,
)


if __name__ == "__main__":
    research_team.print_response(
        "Compare the latest available company and stock information for Tesla, NVIDIA, and Apple."
    )
