from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import Optional, List

from database.session import get_session
from models.blogpost import *
from utils.auth import verify_admin_token

router = APIRouter()

@router.post("/", response_model=BlogPost)
async def create_event(
    data: BlogPostCreate,
    session: Session = Depends(get_session),
    admin_user = Depends(verify_admin_token)
    ) -> BlogPost:

    event = BlogPost(**data.dict())

    session.add(event)
    session.commit()
    session.refresh(event)

    return event

@router.get("/{id}", response_model=BlogPost)
async def read_event(
    id: int,
    session: Session = Depends(get_session)
) -> BlogPost:
    event = session.get(BlogPost, id)

    if not event:
        raise HTTPException(status_code=404, detail="BlogPost not found")

    return event

@router.get("/", response_model=List[BlogPost])
async def read_events(
    session: Session = Depends(get_session),
    skip: int = 0,
    limit: int = 100
) -> List[BlogPost]:

    statement = select(BlogPost).offset(skip).limit(limit)

    events = session.exec(statement).all()
    
    return events

@router.put("/{id}", response_model=BlogPost)
async def update_event(
    id: int,
    data: BlogPostUpdate,
    session: Session = Depends(get_session),
    admin_user = Depends(verify_admin_token)
) -> BlogPost:
    event = session.get(BlogPost, id)

    if not event:
        raise HTTPException(status_code=404, detail="BlogPost not found")
    
    event_data = data.dict(exclude_unset=True)
    for field, value in event_data.items():
        setattr(event, field, value)
    
    session.add(event)
    session.commit()
    session.refresh(event)
    
    return event

@router.delete("/{id}")
async def delete_event(
    id: int,
    session: Session = Depends(get_session),
    admin_user = Depends(verify_admin_token)
) -> dict:
    event = session.get(BlogPost, id)
    if not event:
        raise HTTPException(status_code=404, detail="BlogPost not found")
    
    session.delete(event)
    session.commit()
    
    return {"message": "BlogPost deleted successfully"}