from redis import Redis
from dotenv import load_dotenv
import os

load_dotenv()

redis_host = os.getenv("REDIS_HOST")
redis_port = int(os.getenv("REDIS_PORT"))
redis_password = os.getenv("REDIS_PASSWORD")

def main():

    print(f"Connecting to Redis at {redis_host}:{redis_port}")

    redis = Redis(host=redis_host, port=redis_port, password=redis_password)

    six_months_ttl = 60 * 60 * 24 * 30 * 6

    print(f"Extending all keys with TTL of {six_months_ttl} seconds")

    cursor = 0
    extended = 0
    skipped = 0

    while True:
        cursor, keys = redis.scan(cursor, count=100)
        for key in keys:
            if redis.ttl(key) != -1:  # -1 means no expiry set, skip persistent keys
                redis.expire(key, six_months_ttl)
                extended += 1
            else:
                print(f"Skipping key {key} because it has no TTL")
                skipped += 1
        if cursor == 0:
            break

    print(f"Done. Extended: {extended}, Skipped (no TTL): {skipped}")


if __name__ == "__main__":
    main()
