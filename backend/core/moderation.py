BAD_WORDS = {"fuck", "shit", "ass", "bitch", "nigger"} 

def is_clean(text: str) -> bool:
    lower = text.lower()
    return not any(bad_word in lower for bad_word in BAD_WORDS)
