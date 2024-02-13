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

    def authorization_header(self, request=None) -> str:
        """require authorization header
        - return False"""
        print(request)
        if request is None:
            return None


    def current_user(self, request=None) -> TypeVar("User"):
        """get current user
        - return None"""
        return None
