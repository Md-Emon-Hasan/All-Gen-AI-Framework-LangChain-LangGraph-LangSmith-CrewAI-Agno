"""Streamlit interface for the financial research agent team."""

import os

import streamlit as st
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
    role="Search the web and summarize relevant information with sources.",
    model=web_model,
    tools=[DuckDuckGoTools()],
    markdown=True,
)

finance_agent = Agent(
    name="Financial Analyst",
    role="Answer questions about companies and public market data.",
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
    instructions="Delegate research to the appropriate specialist and synthesize their findings clearly.",
    markdown=True,
)

st.set_page_config(page_title="Financial Research Team", page_icon="📈", layout="centered")
st.title("Financial Research Team")
st.write("Ask a question that needs web research, company information, or stock data.")
st.caption("Research is informational and may use delayed or incomplete market data.")

question = st.text_area(
    "Your question",
    placeholder="Compare the latest available information about Apple and NVIDIA.",
)

if st.button("Research", type="primary", disabled=not question.strip()):
    try:
        with st.spinner("The research team is working…"):
            result = research_team.run(question.strip())
        st.markdown(result.content or "The team did not return a text response.")
    except Exception as exc:
        st.error(f"The request failed: {exc}")
