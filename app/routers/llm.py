from fastapi import APIRouter
from app.schemas.chat import *
from app.services.ollama import chat

router = APIRouter()

@router.post("/chat")
def chat_api(req: ChatRequest):
    answer = chat(req.model, req.prompt)
    return ChatResponse(answer=answer)
