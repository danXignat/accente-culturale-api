from sqlmodel import SQLModel, Field
from typing import Optional

class WorkshopBase(SQLModel):
    title: str
    moto: str
    description: str
    age_range: str
    active: bool = Field(default_factory=True)

class Workshop(WorkshopBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class WorkshopCreate(WorkshopBase):
    pass

class WorkshopUpdate(SQLModel):
    title: Optional[str] = None
    moto: Optional[str] = None
    description: Optional[str] = None
    age_range: Optional[str] = None
    active: Optional[bool] = None