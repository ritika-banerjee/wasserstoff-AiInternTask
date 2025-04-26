from fastapi import FastAPI
from backend.api.routes import router

app = FastAPI(title="GenAI Guessing Game")

app.include_router(router)