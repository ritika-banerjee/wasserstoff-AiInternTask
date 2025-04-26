class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
class GameSession:
    
    def __init__(self, seed_word):
        self.head = Node(seed_word)
        self.tail = self.head
        self.words = set([seed_word])
        self.score = 0
        
    def process_guess(self, guess):
        if guess in self.words:
            return {"status": "Game Over", "messsage" : f"Game Over! '{guess} is already guessed."}    
        
        is_valid = True
        
        if is_valid:
            new_node = Node(guess)
            self.tail.next = new_node
            self.tail = new_node
            self.words.add(guess)
            self.score += 1
            return {"status": "Correct", "message": f"'{guess}' is a valid guess.", "score": self.score}
        
        return {"status": "Invalid", "message": f"'{guess}' is not a valid guess."}
    
    def get_history(self):
        current = self.head
        result = []
        while current:
            result.append(current.value)
            current = current.next
        return result
        
            
    