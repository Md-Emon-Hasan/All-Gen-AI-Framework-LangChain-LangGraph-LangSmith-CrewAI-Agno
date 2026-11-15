"""Serve the financial research agents through the current Agno AgentOS API."""

import os

from agno.agent import Agent
from agno.models.google import Gemini
from agno.os import AgentOS
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

model = Gemini(id=os.getenv("GEMINI_MODEL", "gemini-3.7-flash"))

web_researcher = Agent(
    name="Web Researcher",
    role="Search the web for company news and relevant financial context.",
    model=model,
    tools=[DuckDuckGoTools()],
    markdown=True,
)

market_analyst = Agent(
    name="Market Data Analyst",
    role="Retrieve and explain public-company and stock information.",
    model=model,
    tools=[YFinanceTools(stock_price=True, stock_fundamentals=True, analyst_recommendations=True, company_news=True)],
    markdown=True,
)

research_team = Team(
    name="Financial Research Team",
    model=model,
    members=[web_researcher, market_analyst],
    instructions="Delegate to the right specialist and summarize the results with caveats and sources.",
    markdown=True,
)

agent_os = AgentOS(
    id="agno-financial-research-course",
    agents=[web_researcher, market_analyst],
    teams=[research_team],
)
app = agent_os.get_app()


if __name__ == "__main__":
    agent_os.serve(app="playground:app", reload=True)
