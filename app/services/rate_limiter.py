import time
from functools import wraps

from flask import jsonify, request

from app.extensions import redis_client


def rate_limit(limit, per):
    """Rate-limiting decorator to limit requests per user."""

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            key = f"rl:{request.remote_addr}:{request.endpoint}"
            current_time = time.time()
            window_start = current_time - per

            try:
                # Get the number of requests in the current window
                request_times = redis_client.zrangebyscore(
                    key, window_start, current_time
                )

                # Check if the limit is exceeded
                if len(request_times) >= limit:
                    return jsonify({"error": "Rate limit exceeded"}), 429

                # Add the current request timestamp to the sorted set
                redis_client.zadd(key, {current_time: current_time})

                # Remove older entries outside the current window
                redis_client.zremrangebyscore(key, "-inf", window_start)

                # Set expiration for this key
                redis_client.expire(key, per)

            except Exception as e:
                # Log the error and return a response indicating failure
                print(f"Error while accessing Redis: {e}")
                return jsonify({"error": "Internal Server Error"}), 500

            return f(*args, **kwargs)

        return decorated_function

    return decorator
