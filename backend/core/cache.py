import os
import json
import redis

REDIS_URL = os.getenv("REDIS_URL")

if REDIS_URL:
    r = redis.from_url(REDIS_URL, decode_responses=True)
else:

    REDIS_HOST = os.getenv("REDIS_HOST", "redis")
    REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def get_cached_result(guess, seed, persona="default"):
    key = f"{persona}:{guess}:{seed}"
    raw = r.get(key)
    if raw:
        return json.loads(raw)
    return None

def set_cached_result(guess, seed, result_dict, persona="default"):
    key = f"{persona}:{guess}:{seed}"
    r.set(key, json.dumps(result_dict))
