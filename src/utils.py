"""
Utility functions for the Claude GitHub Integration Test

Provides data validation and processing capabilities.
"""

import re
from typing import Any, Union


def validate_input(data: str) -> bool:
    """
    Validate input data format.
    
    Args:
        data: Input string to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not data or len(data.strip()) == 0:
        return False
    
    # Check for basic alphanumeric pattern
    pattern = r'^[a-zA-Z0-9\s\-_]+$'
    return bool(re.match(pattern, data))


def process_data(data: str) -> Union[str, None]:
    """
    Process input data and return formatted result.
    
    Args:
        data: Valid input string
        
    Returns:
        Union[str, None]: Processed data or None if processing fails
    """
    try:
        # Simple processing: uppercase and add timestamp
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        processed = f"[{timestamp}] {data.upper().strip()}"
        return processed
        
    except Exception as e:
        print(f"Processing error: {e}")
        return None


def calculate_hash(data: str) -> str:
    """
    Calculate a simple hash for the input data.
    
    Args:
        data: Input string
        
    Returns:
        str: Hexadecimal hash string
    """
    import hashlib
    return hashlib.md5(data.encode()).hexdigest()
