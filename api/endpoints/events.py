from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_events():
    return {"miau": "hau"}