from fastapi import APIRouter, Request
from backend.core.game_logic import GameSession

router = APIRouter()
session = GameSession(seed_word="Rock")

@router.post("/guess")
async def make_guess(request: Request):
    data = await request.json()
    guess = data.get("guess")
    response = session.process_guess(guess)
    return response

@router.get("/history")
async def get_history():
    return {"guesses": session.get_history()}