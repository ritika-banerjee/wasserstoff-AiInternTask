from backend.core.ai_client import validate_guess
from backend.core.moderation import is_clean
from backend.db.models import increment_global_guess_count, get_global_guess_count  

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class GameSession:
    def __init__(self, seed_word: str):
        self.head = Node(seed_word)
        self.tail = self.head
        self.word_set = set([seed_word])
        self.score = 0

    async def process_guess(self, guess: str, persona: str = "default") -> dict:
        guess = guess.strip().capitalize()

        # 1. Duplicate guess check
        if guess in self.word_set:
            return {
                "status": "game_over",
                "message": f"❌ Game Over! '{guess}' was already guessed."
            }

        # 2. Cleanliness check 
        if not is_clean(guess):
            return {
                "status": "blocked",
                "message": "🚫 Your guess contains inappropriate content."
            }

        # 3. Ask the AI
        ai_result = await validate_guess(guess, self.tail.value, persona)
        verdict = ai_result["verdict"]
        explanation = ai_result["message"]

        if verdict == "YES":
            # 4. Update linked list
            new_node = Node(guess)
            self.tail.next = new_node
            self.tail = new_node
            self.word_set.add(guess)
            self.score += 1

            # 5. Increment global guess count in DB
            global_count = increment_global_guess_count(guess)

            return {
                "status": "success",
                "message": f"✅ Nice! {explanation} '{guess}' has been guessed {global_count} times before.",
                "score": self.score,
                "last_five": self.get_last_five(),
            }

        elif verdict == "NO":
            return {
                "status": "fail",
                "message": f"❌ {explanation}"
            }

        elif verdict == "BLOCKED":
            return {
                "status": "blocked",
                "message": explanation
            }

        else:
            return {
                "status": "error",
                "message": f"🤖 Couldn't decide: {explanation}"
            }

    def get_history(self) -> list:
        current = self.head
        history = []
        while current:
            history.append(current.value)
            current = current.next
        return history

    def get_last_five(self) -> list:
        history = self.get_history()
        return history[-5:]

    def reset(self):
        seed = self.head.value
        self.__init__(seed_word=seed)
