from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.api.routes import router
from backend.db.models import init_db
import os
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db() 
    yield 

app = FastAPI(title="GenAI Guessing Game",lifespan=lifespan)


# Include API routes
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Serve static frontend
frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend"))
app.mount("/", StaticFiles(directory=frontend_path, html=True), name="static")
