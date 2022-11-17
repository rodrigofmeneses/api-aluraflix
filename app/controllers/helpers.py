from functools import wraps
from app.models import User
from flask import jsonify, request, url_for


def token_required_decorator(f):
    """Authenticate user with valid Token
    return: Error message if token is not valid.
    """
    @wraps(f)
    def decorator(*args, **kwargs):
        """Get token by Request and return the user or error message"""
        auth_token = request.headers.get("Authorization") or "Invalid"
        token_value = User.decode_auth_token(auth_token.split()[-1])

        if (
            isinstance(token_value, str)
            and ("Signature expired" in token_value 
            or "Invalid token" in token_value)
        ):
            return jsonify({"message": f"User not authorized! {token_value}"}), 401
        return f(*args, **kwargs)

    return decorator

def token_required():
    """Get token by Request and return the user or error message"""
    free_routes = [
        url_for('auth.authenticate'), 
        url_for('auth.register'),
        # url_for('videos.free'),
    ]

    if request.endpoint and not request.url_rule.rule in free_routes:
        auth_token = request.headers.get("Authorization") or "Invalid"
        token_value = User.decode_auth_token(auth_token)

        if (
            isinstance(token_value, str)
            and ("Signature expired" in token_value 
            or "Invalid token" in token_value)
        ):
            return jsonify({"message": f"User not authorized! {token_value}"}), 401