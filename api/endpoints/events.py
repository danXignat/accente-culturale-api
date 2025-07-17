from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import Optional, List

from database.session import get_session
from models.event import *
from utils.auth import verify_admin_token

router = APIRouter()

@router.post("/", response_model=Event)
async def create_event(
    data: EventCreate,
    session: Session = Depends(get_session),
    admin_user = Depends(verify_admin_token)
    ) -> Event:

    event = Event(**data.dict())

    session.add(event)
    session.commit()
    session.refresh(event)

    return event

@router.get("/{id}", response_model=Event)
async def read_event(
    id: int,
    session: Session = Depends(get_session)
) -> Event:
    event = session.get(Event, id)

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    return event

@router.get("/", response_model=List[Event])
async def read_events(
    session: Session = Depends(get_session),
    skip: int = 0,
    limit: int = 100
) -> List[Event]:

    statement = select(Event).offset(skip).limit(limit)

    events = session.exec(statement).all()
    
    return events

@router.put("/{id}", response_model=Event)
async def update_event(
    id: int,
    data: EventUpdate,
    session: Session = Depends(get_session),
    admin_user = Depends(verify_admin_token)
) -> Event:
    event = session.get(Event, id)

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    
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
    event = session.get(Event, id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    session.delete(event)
    session.commit()
    
    return {"message": "Event deleted successfully"}