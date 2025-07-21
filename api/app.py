from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from database.session import create_db_and_tables
from api.endpoints import events, workshops, auth, blogposts

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(events.router     , prefix="/events"      , tags=["Events"])
api_router.include_router(workshops.router  , prefix="/workshops"   , tags=["Workshops"])
api_router.include_router(blogposts.router  , prefix="/blogposts"   , tags=["BlogPosts"])
api_router.include_router(auth.router       , prefix="/auth"        , tags=["Authentication"])
app.include_router(api_router)

@app.get("/")
async def home():
    return {"home": "Hello"}