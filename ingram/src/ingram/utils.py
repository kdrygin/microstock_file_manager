import re
from pathlib import Path

def sanitize_filename(name: str, max_length: int = 120) -> str:
    """Clean filename for microstock platforms"""
    # Replace bad characters
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    name = re.sub(r'\s+', '_', name.strip())
    name = name.lower()
    
    if len(name) > max_length:
        name = name[:max_length]
    
    return name