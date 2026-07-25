from pathlib import Path
from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter()

@router.get("/help", response_class=PlainTextResponse)
def help():
    return Path("docs/API.md").read_test(encoding="utf-8")
