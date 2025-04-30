from fastapi import APIRouter, Request, Query, Header
from backend.core.game_logic import GameSession

router = APIRouter()

session = GameSession(seed_word="Rock")

@router.post("/guess")
async def make_guess(
    request: Request,
    persona: str = Query("default", enum=["default", "cheery", "serious"]),
    host_persona: str = Header(None)
):
    """
    POST /guess
    {
      "guess": "Paper"
    }

    Optional persona can be passed as:
    - query param: /guess?persona=cheery
    - or header: host-persona: cheery
    """

    try:
        data = await request.json()
        guess = data.get("guess", "").strip()

        if not guess:
            return {"status": "error", "message": "No guess provided."}

        active_persona = host_persona or persona

        result = await session.process_guess(guess, persona=active_persona)
        return result

    except Exception as e:
        print(f"[Route Error] {e}")
        return {
            "status": "error",
            "message": "Something went wrong. Try again."
        }

@router.get("/history")
def get_guess_history():
    """
    Returns all previous guesses in order
    """
    return {
        "guesses": session.get_history(),
        "score": session.score
    }

@router.get("/reset")
def reset_game():
    """
    Resets the game 
    """
    session.reset()
    return {"status": "reset", "message": "Game reset to seed word."}
