from datetime import date
from sqlmodel import SQLModel, Field
from typing import Optional

class BlogPostBase(SQLModel):
    title: str
    content: str

class BlogPost(BlogPostBase, table=True):
    publish_date: date = Field(default_factory=date.today)
    id: int | None = Field(default=None, primary_key=True)

class BlogPostCreate(BlogPostBase):
    pass

class BlogPostUpdate(SQLModel):
    title: Optional[str] = None
    content: Optional[str] = None