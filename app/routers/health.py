from fastapi import APIROUTER

router = APIRouter()

@router.get("/health")
def health():
    return { "status": "OK" }
