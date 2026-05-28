import os
from pathlib import Path

class Config:
    # Base paths
    ROOT_DIR = Path(__file__).parent.parent.parent
    DATA_DIR = ROOT_DIR / "data"
    
    # Microstock naming rules
    MAX_FILENAME_LENGTH = 120
    SEPARATOR = "_"
    
    # Default keywords (you can expand later)
    DEFAULT_KEYWORDS = ["stock", "photo", "microstock"]