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

    KEYWORDS_PATH = os.path.expanduser("~/Google Drive/My Drive/Biz/Keywords/keywords.json")
    # KEYWORDS_PATH = "~/Google Drive/My Drive/Biz/Keywords/keywords.json"
    # KEYWORDS_PATH = "/Users/kdrygin/Projects/microstock_file_manager/ingram/data/keywords_example.json"
    
    IMAGE_PATTERNS = ["*.jpg", "*.png"]