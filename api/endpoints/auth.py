import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, status, APIRouter

from schemas.auth import *
from utils.auth import verify_admin_credentials
from core.config import settings

router = APIRouter()

@router.post("/admin/login")
async def admin_login(credentials: AdminCredentials) -> Token:
    if not verify_admin_credentials(credentials):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token_data = {
        "sub": credentials.username,
        "role": "admin",
        "exp": datetime.utcnow() + timedelta(hours=24)
    }
    
    token = jwt.encode(token_data, settings.JWT_SECRET_KEY, algorithm="HS256")

    return Token(access_token=token, token_type="bearer")