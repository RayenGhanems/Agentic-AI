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
# if you prefer to load .env for the shell first:
# set -a; source .env; set +a
```
LangServe will start (default port 8000) with docs at `http://localhost:8000/docs`.

## Example invocation
Call the mounted route:
```bash
curl -X POST http://localhost:8000/openai_prompter/invoke \
  -H "Content-Type: application/json" \
  -d '{"input": {"objective": "Draft a prompt for an agent that summarizes meeting notes into bullet points"}}'
```
You’ll get back a rewritten prompt based on the guidance in `Prompter.txt`.

## What to customize
- Edit `Prompter.txt` with your own prompt-engineering heuristics.
- Tweak model parameters in `app/chain.py` (e.g., model name, temperature, output format).
- Change the mounted path in `app/server.py` if you want a different endpoint prefix.
