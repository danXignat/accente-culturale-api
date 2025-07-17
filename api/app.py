from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from contextlib import asynccontextmanager

from api.endpoints import events, workshops, auth
from database.session import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://localhost:4200"],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["Content-Type"],
)

app.include_router(events.router, prefix="/events", tags=["Events"])
app.include_router(workshops.router, prefix="/workshops", tags=["Workshops"])
app.include_router(auth.router, prefix="/auth", tags=["Authentification"])

@app.get("/")
async def home():
    return {"home": "Hello"}

@app.on_event("startup")
async def startup_event():
    print("🚀 App is starting...")

@app.on_event("shutdown")
async def shutdown_event():
    print("🛑 App is shutting down...")