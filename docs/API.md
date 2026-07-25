# CSSLab LLM API

## Overview

CSSLab LLM Servers provides a unified REST interface to multiple local LLMs running on Ollama servers.

---

## GET /

Returns server information.

---

## GET /health

Returns server health.

Response

```json
{
    "status":"OK"
}
```

---

## GET /models

Returns supported models.

```json
[
    "qwen",
    "deepseek",
    "gemma"
]
```

---

## GET /help

Returns this document.

---

## POST /chat

Request

```json
{
    "model":"qwen",
    "prompt":"Hello"
}
```

Response

```json
{
    "answer":"Hello!"
}
```

Supported models

- qwen
- deepseek
- gemma

---

Future APIs

POST /ocr

POST /vision

POST /receipt

POST /hwpx

POST /inspection
