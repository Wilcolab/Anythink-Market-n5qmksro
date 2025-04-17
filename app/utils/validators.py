import re
from typing import Any, Optional

class InputValidator:
    @staticmethod
    def sanitize_string(value: Optional[str]) -> Optional[str]:
        """Sanitize string input by removing dangerous characters"""
        if value is None:
            return None
        # Remove any non-alphanumeric characters except common punctuation
        sanitized = re.sub(r'[^a-zA-Z0-9\s\-_.,!?@]', '', value)
        return sanitized.strip()

    @staticmethod
    def validate_query_tag(tag: str) -> bool:
        """Validate query tag format"""
        if not tag:
            return False
        # Only allow alphanumeric and underscore
        return bool(re.match(r'^[a-zA-Z0-9_]+$', tag))

    @staticmethod
    def validate_username(username: str) -> bool:
        """Validate username format"""
        if not username:
            return False
        # Only allow alphanumeric and underscore, 3-30 characters
        return bool(re.match(r'^[a-zA-Z0-9_]{3,30}$', username))
