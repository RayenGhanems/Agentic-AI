# OpenAI Prompter

Generate cleaner prompts using OpenAI’s prompt-engineering guidelines. The helper chain reads guidance from `Prompter.txt` (copied from https://platform.openai.com/docs/guides/prompt-engineering) and rewrites your objective into a structured, higher-quality prompt.

## How it works
- `Prompter.txt` contains prompt-engineering tips.
- `app/chain.py` loads that file and builds a chain: prompt template → `ChatOpenAI` → string output.
- `app/server.py` mounts the chain at `/openai_prompter` via LangServe. You can invoke it with REST or the LangServe UI.

## Setup
1) Create/activate an environment (example with conda):
```bash
conda create -n openai-prompter python=3.11 -y
conda activate openai-prompter
```
2) Install dependencies (pip/poetry both work):
```bash
pip install -r requirements.txt

```

## Environment variables
Set your keys in the shell or place them in `.env` (already loaded by `app/server.py`):
```bash
export OPENAI_API_KEY=<your-openai-key>
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY=<your-langsmith-key>
export LANGSMITH_PROJECT=<your-project>  # optional, defaults to "default"
```
Or create `.env` in the project root:
```
OPENAI_API_KEY=...
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=...
LANGSMITH_PROJECT=openai-prompter
```

## Run the server
From the project root:
```bash
langchain serve
```
LangServe will start and you can check enter directly to the link below to test the agent yourself:
```bash
http://localhost:8000/openai_prompter/playground/
```


