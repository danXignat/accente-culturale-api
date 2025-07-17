from pydantic import BaseModel

class AdminCredentials(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class ItemCreate(BaseModel):
    name: str
    description: str

class ItemUpdate(BaseModel):
    name: str | None = None
    description: str | None = None