from sqlmodel import SQLModel, Field
from typing import Optional
import datetime

class EventBase(SQLModel):
    title: str
    description: str
    date: datetime.date

class Event(EventBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class EventCreate(EventBase):
    pass

class EventUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    date: Optional[datetime.date] = None