from fastapi import APIRouter
from app.config import MODEL_SERVERS

router = APIRouter()

@router.get("/models")
def models():
    return list(MODEL_SERVERS.keys())
