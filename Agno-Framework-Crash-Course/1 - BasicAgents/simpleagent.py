"""Run a single Gemini assistant with DuckDuckGo search."""

import os

from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    name="Web Research Assistant",
    model=Gemini(id=os.getenv("GEMINI_MODEL", "gemini-3.7-flash")),
    tools=[DuckDuckGoTools()],
    instructions="Answer clearly. Use web search for current information and cite useful sources.",
    markdown=True,
)


if __name__ == "__main__":
    agent.print_response("Where is the United States, and what are its neighboring countries?")
