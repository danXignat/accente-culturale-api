import jwt
import bcrypt
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException

from services.auth import admin_security
from schemas.auth import *
from core.config import settings

def verify_admin_credentials(credentials: AdminCredentials) -> bool:
    if credentials.username != settings.ADMIN_USERNAME:
        return False
    stored_hash = settings.ADMIN_PASSWORD.encode('utf-8')
    return bcrypt.checkpw(credentials.password.encode('utf-8'), stored_hash)

async def verify_admin_token(credentials: HTTPAuthorizationCredentials = Depends(admin_security)):
    try:
        payload = jwt.decode(credentials.credentials, settings.JWT_SECRET_KEY, algorithms=["HS256"])
        if payload.get("role") != "admin":
            raise HTTPException(status_code=403, detail="Admin access required")
        return payload
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid admin token")