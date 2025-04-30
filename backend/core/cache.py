import redis
import json

r = redis.Redis(host="redis", port=6379, decode_responses=True)

def get_cached_result(guess, seed, persona="default"):
    key = f"{persona}:{guess}:{seed}"
    raw = r.get(key)
    if raw:
        return json.loads(raw)
    return None

def set_cached_result(guess, seed, result_dict, persona="default"):
    key = f"{persona}:{guess}:{seed}"
    r.set(key, json.dumps(result_dict))
