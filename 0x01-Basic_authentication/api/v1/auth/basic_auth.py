#!/usr/bin/env python3
"""Basic Auth"""
import re
import base64
import binascii

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """a class BasicAuth that inherits from Auth"""
    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """Returns base64"""
        if isinstance(authorization_header, str):
            pattern = r'Basic (?P<token>.+)'
            match = re.fullmatch(pattern, authorization_header.strip())
            if match is not None:
                return match.group('token')
            return None

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """Returns Base64 decode"""
        if isinstance(base64_authorization_header, str):
            try:
                decoded = base64.b64decode(
                    base64_authorization_header,
                    validate=True
                )
                return decoded.decode('utf-8')
            except (binascii.Error, UnicodeDecodeError):
                return None
