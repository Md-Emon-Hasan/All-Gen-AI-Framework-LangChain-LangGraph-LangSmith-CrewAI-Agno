# LangSmith Crash Course

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Examples-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)](https://www.langchain.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Workflow-1C3C3C?style=for-the-badge)](https://www.langchain.com/langgraph)
[![LangSmith](https://img.shields.io/badge/LangSmith-Tracing-00A67E?style=for-the-badge)](https://www.langchain.com/langsmith)
[![Apache 2.0](https://img.shields.io/badge/License-Apache--2.0-blue?style=for-the-badge)](../LICENSE)

<p align="center"><img src="https://github.com/user-attachments/assets/e0fac8eb-212e-4a66-95de-23db91194a4c" alt="LangSmith Crash Course banner" width="100%"></p>

A small, hands-on collection showing LangChain applications and LangSmith tracing. The examples progress from a basic model call to chains, PDF retrieval, a tool-using agent, and a LangGraph workflow. LangSmith is used for tracing and observability; LangChain and LangGraph provide the application and workflow abstractions.

## Lessons

| File | Example |
| --- | --- |
| `1_simple_llm_call.py` | Prompt, chat model, and output parser composed as a runnable chain. |
| `2_sequential_chain.py` | Two prompt/model steps composed into a sequential chain. |
| `3_rag_v1.py` | PDF loading, chunking, OpenAI embeddings, FAISS retrieval, and question answering over a local `islr.pdf` file. |
| `3_rag_v2.py`–`3_rag_v4.py` | Iterations of the RAG example. |
| `4_agent.py` | A ReAct agent with web search and a weather tool. |
| `5_langgraph.py` | Parallel essay evaluation with LangGraph, structured output, and LangSmith trace annotations. |

## Requirements

- Python 3.10 or newer is recommended.
- A virtual environment is recommended to isolate the pinned dependencies in `requirements.txt`.
- An OpenAI API key is needed for model and embedding examples.
- A LangSmith API key is needed only if you enable LangSmith tracing.
- The RAG examples need a local PDF named `islr.pdf` in this directory. You can download the ISLR book from the [authors' official site](https://www.statlearning.com/) for your own use; the PDF is not included in this repository.
- The search and weather tools in the agent example need internet access and their respective service credentials.

## Setup

From this directory, create and activate a virtual environment:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

On macOS or Linux, activate with `source .venv/bin/activate` instead.

Create a local `.env` file in this directory for the credentials used by your chosen example:

```dotenv
OPENAI_API_KEY=your_openai_api_key
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_PROJECT=langsmith-crash-course
WEATHERSTACK_API_KEY=your_weatherstack_api_key
```

Only add credentials needed by the selected lesson. LangSmith tracing can be enabled in the LangSmith dashboard or with the environment variables above. Do not commit `.env` or share a notebook/script output containing a credential.

## Run an example

Run scripts from this directory so the local `.env` file is loaded:

```bash
python 1_simple_llm_call.py
python 2_sequential_chain.py
python 3_rag_v1.py
python 4_agent.py
python 5_langgraph.py
```

The RAG script expects your local `islr.pdf` file in this directory. The agent makes external search and weather requests. Review the scripts before running them, and check the required keys and provider usage limits.

## Notes

- These lessons use framework APIs that can change. If a dependency update breaks an example, consult the current package documentation and adjust the code for the installed versions.
- `requirements.txt` pins a course environment; installing it can take time and may not suit every operating system.
- Some model and search requests may incur costs or be subject to service limits.

## License

This course is part of the repository distributed under the [Apache License 2.0](../LICENSE).

## Connect with me

- **Portfolio:** [emonlabs-ai.hitechparks.com](https://emonlabs-ai.hitechparks.com)
- **GitHub:** [Md-Emon-Hasan](https://github.com/Md-Emon-Hasan)
- **LinkedIn:** [Md Emon Hasan](https://www.linkedin.com/in/md-emon-hasan-695483237/)
- **Hugging Face:** [emonHasan01](https://huggingface.co/emonHasan01)
- **Email:** [emon.mlengineer@gmail.com](mailto:emon.mlengineer@gmail.com)
- **WhatsApp:** [+880 1834-363533](https://wa.me/8801834363533)
