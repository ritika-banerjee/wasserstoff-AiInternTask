import google.generativeai as genai
from backend.core.cache import get_cached_result, set_cached_result
from backend.core.moderation import is_clean
import os
from dotenv import load_dotenv
import json

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Define the model
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# Prompt builder based on persona
def build_prompt(guess: str, seed: str, persona: str = "default") -> str:
    persona_prefix = {
        "cheery": "Be friendly and encouraging. In 1 sentence, say if",
        "serious": "Be concise and analytical. In 1 sentence, say if",
        "default": "Briefly say if"
    }
    base = persona_prefix.get(persona.lower(), persona_prefix["default"])
    return f"{base} '{guess}' beats '{seed}' metaphorically. Be creative but say YES or NO clearly."

# Main AI validation function
async def validate_guess(guess: str, seed: str, persona: str = "default") -> dict:
    if not is_clean(guess):
        return {
            "verdict": "BLOCKED",
            "message": "Your guess contains disallowed content. Try something else."
        }

    key = f"{persona}:{guess}:{seed}"

    # Check Redis cache
    cached = get_cached_result(guess, seed, persona)
    if cached:
        return cached

    prompt = build_prompt(guess, seed, persona)

    try:
        response = model.generate_content(
            [prompt],
            generation_config={
                "temperature": 0.7,
                "top_p": 1,
                "top_k": 1,
                "max_output_tokens": 100
            }
        )

        full_response = response.text.strip()

        if "yes" in full_response.lower():
            verdict = "YES"
        elif "no" in full_response.lower():
            verdict = "NO"
        else:
            verdict = "UNKNOWN"

        result = {
            "verdict": verdict,
            "message": full_response
        }

        set_cached_result(guess, seed, result, persona)
        return result

    except Exception as e:
        print(f"[Gemini Error] {e}")
        return {
            "verdict": "ERROR",
            "message": "AI could not respond. Try again."
        }
