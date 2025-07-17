from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import Optional, List

from database.session import get_session
from models.workshop import *
from utils.auth import verify_admin_token

router = APIRouter()

@router.post("/", response_model=Workshop)
async def create_workshop(
    data: WorkshopCreate,
    session: Session = Depends(get_session),
    admin_user = Depends(verify_admin_token)
    ) -> Workshop:

    workshop = Workshop(**data.dict())

    session.add(workshop)
    session.commit()
    session.refresh(workshop)

    return workshop

@router.get("/{id}", response_model=Workshop)
async def read_workshop(
    id: int,
    session: Session = Depends(get_session),
) -> Workshop:
    workshop = session.get(Workshop, id)

    if not workshop:
        raise HTTPException(status_code=404, detail="Workshop not found")

    return workshop

@router.get("/", response_model=List[Workshop])
async def read_workshops(
    session: Session = Depends(get_session),
    skip: int = 0,
    limit: int = 100
) -> List[Workshop]:
    statement = select(Workshop).offset(skip).limit(limit)

    workshops = session.exec(statement).all()
    
    return workshops

@router.put("/{id}", response_model=Workshop)
async def update_workshop(
    id: int,
    data: WorkshopUpdate,
    session: Session = Depends(get_session),
    admin_user = Depends(verify_admin_token)
) -> Workshop:
    workshop = session.get(Workshop, id)

    if not workshop:
        raise HTTPException(status_code=404, detail="Workshop not found")
    
    workshop_data = data.dict(exclude_unset=True)
    for field, value in workshop_data.items():
        setattr(workshop, field, value)
    
    session.add(workshop)
    session.commit()
    session.refresh(workshop)
    
    return workshop

@router.delete("/{id}")
async def delete_workshop(
    id: int,
    session: Session = Depends(get_session),
    admin_user = Depends(verify_admin_token)
) -> dict:
    workshop = session.get(Workshop, id)
    if not workshop:
        raise HTTPException(status_code=404, detail="Workshop not found")
    
    session.delete(workshop)
    session.commit()
    
    return {"message": "Workshop deleted successfully"}