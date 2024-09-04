"""
Auth module
"""
from flask import request
from typing import List, TypeVar

class Auth:
    """
    Auth class
    """
    def __init__(self):
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Require Auth
        """
        if path is None or excluded_paths is None or excluded_paths is []:
            return True

        normalized_path = path.rstrip('/')

        for excluded_path in excluded_paths:
            normalized_excluded_path = excluded_path.rstrip('/')
            if normalized_path == normalized_excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        return None
