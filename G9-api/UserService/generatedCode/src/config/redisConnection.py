import os
import redis


def connection():
    return redis.Redis(
        host=os.getenv('REDIS_HOST'),
        port=os.getenv('REDIS_PORT'),
        username=os.getenv('REDIS_USER'),
        password=os.getenv('REDIS_PASS'),
        db=0
    )
