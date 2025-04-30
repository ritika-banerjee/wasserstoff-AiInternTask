from fastapi import FastAPI
from backend.api.routes import router
from backend.db.models import init_db
from fastapi.staticfiles import StaticFiles
import os

init_db()

app = FastAPI(title="GenAI Guessing Game")

# Include API routes
app.include_router(router)

# Serve static frontend
frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend"))
app.mount("/", StaticFiles(directory=frontend_path, html=True), name="static")
