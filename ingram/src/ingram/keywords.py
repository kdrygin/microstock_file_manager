import json
from pathlib import Path
from typing import Dict, Any

from .config import Config


def load_keywords(path: Path | str | None = None) -> Dict[str, Any]:
    """
    Load keywords data from specified path.
    
    Args:
        path: Path to the keywords JSON file.
              If None, uses Config.KEYWORDS_PATH by default.
    
    Returns:
        Dictionary from "data"."items"
    """
    if path is None:
        path = Path(Config.KEYWORDS_PATH)
    else:
        path = Path(path)
    
    if not path.exists():
        raise FileNotFoundError(f"Keywords file not found: {path}")
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Extract "data"."items"
        items = data.get("data", {}).get("items")
        
        if items is None:
            raise ValueError(f"Invalid keywords structure in {path}: 'data.items' key not found")
        
        if not isinstance(items, dict):
            raise ValueError(
                f"'data.items' should be a dict, got {type(items).__name__} in {path}"
            )
        
        return items
        
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format in {path}: {e}") from e
    except Exception as e:
        raise RuntimeError(f"Failed to load keywords from {path}: {e}") from e