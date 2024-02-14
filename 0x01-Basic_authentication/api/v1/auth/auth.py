#!/usr/bin/env python3
"""
Route module for Auth
"""
from typing import List, TypeVar


class Auth:
    """auth class for authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require authentication
        return
            - False"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != "/":
            path += "/"

        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """require authorization header
        - return False"""
        print(request)
        if request is None:
            return None

        val = request.headers.get("Authorization", None)
        if val:
            return val
        else:
            return None

    def current_user(self, request=None) -> TypeVar("User"):
        """get current user
        - return None"""
        return None
