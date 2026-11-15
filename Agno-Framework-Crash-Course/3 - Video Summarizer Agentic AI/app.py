"""Analyze uploaded video files with a Gemini multimodal agent."""

import os
import tempfile
from pathlib import Path

import streamlit as st
from agno.agent import Agent
from agno.media import Video
from agno.models.google import Gemini
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Video Summarizer", page_icon="🎬", layout="wide")
st.title("Video Summarizer")
st.write("Upload a video and ask Gemini to describe or summarize its contents.")

if not os.getenv("GOOGLE_API_KEY"):
    st.error("Add GOOGLE_API_KEY to the root .env file, then restart Streamlit.")
    st.stop()


@st.cache_resource
def get_agent() -> Agent:
    return Agent(
        name="Video Summarizer",
        model=Gemini(id=os.getenv("GEMINI_MODEL", "gemini-3.7-flash")),
        instructions="Analyze the attached video and answer the user's question with clear, useful details.",
        markdown=True,
    )


uploaded_video = st.file_uploader(
    "Choose a video",
    type=["mp4", "mov", "avi"],
    help="Choose a video format supported by your Gemini model and Google account.",
)

if uploaded_video:
    st.video(uploaded_video)
    question = st.text_area(
        "What would you like to know?",
        placeholder="Summarize the video and identify the key moments.",
    )

    if st.button("Analyze video", type="primary", disabled=not question.strip()):
        suffix = Path(uploaded_video.name).suffix or ".mp4"
        temp_path = None
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_video:
                temp_video.write(uploaded_video.getvalue())
                temp_path = temp_video.name

            with st.spinner("Gemini is analyzing the video…"):
                result = get_agent().run(
                    question.strip(),
                    videos=[Video(filepath=temp_path)],
                )

            st.subheader("Analysis")
            st.markdown(result.content or "The model did not return a text response.")
        except Exception as exc:
            st.error(f"Video analysis failed: {exc}")
        finally:
            if temp_path:
                Path(temp_path).unlink(missing_ok=True)
