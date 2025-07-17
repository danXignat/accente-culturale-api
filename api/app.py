from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.endpoints import events, workshops

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with allowed origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(events.router, prefix="/events", tags=["Events"])
app.include_router(workshops.router, prefix="/workshops", tags=["Workshops"])

@app.get("/")
async def home():
    return {"home": "Hello"}

@app.on_event("startup")
async def startup_event():
    print("🚀 App is starting...")

@app.on_event("shutdown")
async def shutdown_event():
    print("🛑 App is shutting down...")