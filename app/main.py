from fastapi import FastAPI
from app.routers import health
from app.routers import models
from app.routers import llm
from app.routers import help

app = FastAPI(title="CSSLab-LLM-Server", version="1.0")

@app.get("/")
def index():
    return { "name": "CSSLab-LLM-Server", "version": "1.0", "help": "/help", "docs": "/docs", "models": "/models" }

app.include_router(health.router)
app.include_router(models.router)
app.include_router(llm.router)
app.include_router(help.router)
