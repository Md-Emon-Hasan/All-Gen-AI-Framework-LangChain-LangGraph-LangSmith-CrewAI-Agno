"""Build a financial research team using Gemini, web search, and yfinance."""

import os

from agno.agent import Agent
from agno.models.google import Gemini
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

model = Gemini(id=os.getenv("GEMINI_MODEL", "gemini-3.7-flash"))

web_researcher = Agent(
    name="Web Researcher",
    role="Find current company news and other relevant information on the web.",
    model=model,
    tools=[DuckDuckGoTools()],
    instructions=[
        "Use web search for current claims.",
        "Include source links when available.",
        "Keep the summary concise and separate facts from interpretation.",
    ],
    markdown=True,
)

market_analyst = Agent(
    name="Market Data Analyst",
    role="Retrieve available stock prices, fundamentals, recommendations, and company news.",
    model=model,
    tools=[
        YFinanceTools(
            stock_price=True,
            stock_fundamentals=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
        )
    ],
    instructions="Use tables for comparable values and identify the company ticker when possible.",
    markdown=True,
)

financial_research_team = Team(
    name="Financial Research Team",
    model=model,
    members=[web_researcher, market_analyst],
    instructions=[
        "Ask the appropriate specialist for web or market data research.",
        "Combine their findings into a readable report with source links and clear caveats.",
        "Do not present the report as personalized investment advice.",
    ],
    markdown=True,
)


if __name__ == "__main__":
    financial_research_team.print_response(
        "Summarize the latest available stock metrics, analyst recommendations, and recent news for NVIDIA (NVDA).",
        stream=True,
    )
