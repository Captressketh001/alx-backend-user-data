#!/usr/bin/env python3
"""Session Auth"""

from uuid import uuid4
from .auth import Auth


class SessionAuth(Auth):
    """a class SessionAuth that inherits from Auth"""
    user_id_by_session_id = dict()

    def create_session(self, user_id: str = None) -> str:
        """Create a session id"""
        if isinstance(user_id, str):
            session_id = str(uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id
