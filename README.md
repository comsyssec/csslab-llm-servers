# CSSLab LLM Server AI Gateway

CSSLab LLM Server AI Gateway is a FastAPI-based REST server that provides a unified interface to multiple Ollama servers.

Current models

| Name | Model |
|------|-------|
| qwen | qwen2.5:14b |
| deepseek | deepseek-r1:14b |
| gemma | gemma3:12b |

---

## Install

```bash
pip install -r requirements.txt
```

---

## Run

```bash
uvicorn app.main:app \
    --host 0.0.0.0 \
    --port 8000
```

---

## API

Swagger

```
http://SERVER:8000/docs
```

Redoc

```
http://SERVER:8000/redoc
```

Help

```
http://SERVER:8000/help
```

---

## Example

```bash
curl \
-X POST \
http://localhost:8000/chat \
-H "Content-Type: application/json" \
-d '{
    "model":"qwen",
    "prompt":"What is AI?"
}'
```

---

## Available Models

- qwen
- deepseek
- gemma

---

## Roadmap

- OCR API
- Vision API
- HWPX Generator
- Receipt Parser
- KENTECH Automation
- Agent Workflow
