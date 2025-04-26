import redis
import os

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def get_cached_result(guess, seed):
    return r.get(f"{guess} : {seed}")

def set_cached_result(guess, seed, result):
    r.set(f"{guess} : {seed}", result)