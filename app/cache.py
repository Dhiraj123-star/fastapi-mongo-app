import os
import json
import logging
from valkey import Valkey
from dotenv import load_dotenv

load_dotenv()

VALKEY_HOST = os.getenv("VALKEY_HOST", "valkey")
VALKEY_PORT = int(os.getenv("VALKEY_PORT", "6379"))

cache = Valkey(
    host=VALKEY_HOST,
    port=VALKEY_PORT,
    decode_responses=True
)

def get_cache_key(email:str)->str:
    return f"user:{email}"

async def get_user_from_cache(email:str):
    key= get_cache_key(email)
    cached_data = cache.get(key)
    if cached_data:

        logging.info(f"✅ Cache hit for user: {email}")
        return json.loads(cached_data)
    logging.info(f"❌ Cache miss for user: {email}")

    return None

async def set_user_to_cache(email:str, user_data:dict):
    key = get_cache_key(email)
    cache.set(key, json.dumps(user_data),ex=300) # 5 min TTL
    logging.info(f"✅ User data cached for: {email}")

async def invalidate_user_cache(email:str):
    key= get_cache_key(email)
    cache.delete(key)
    logging.info(f"♻️ Cache invalidated for user: {email}")    
