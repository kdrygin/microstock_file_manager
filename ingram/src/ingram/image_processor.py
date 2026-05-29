import json
import re
from pathlib import Path
from typing import Dict, Any, Optional

from .config import Config
from .keywords import load_keywords


def extract_image_name(filename: str) -> str:
    """
    Extract image name from filename by removing extension and trailing numbers/parentheses.

    Examples:
        "green robot (1).jpg" -> "green robot"
        "red apple.png" -> "red apple"
    """
    # Remove extension
    name = Path(filename).stem

    # Remove trailing numbers in parentheses like " (1)", " (2)", etc.
    name = re.sub(r'\s*\(\d+\)\s*$', '', name)

    # Strip any trailing whitespace
    name = name.strip()

    return name


def load_image_descriptions(folder_path: Path | str) -> Dict[str, Any]:
    """
    Load image descriptions from JSON file in the specified folder.
    Creates a new empty dict if file doesn't exist.

    Args:
        folder_path: Path to the folder containing image_description.json

    Returns:
        Dictionary with image descriptions
    """
    folder_path = Path(folder_path)
    desc_file = folder_path / "image_description.json"

    if desc_file.exists():
        try:
            with open(desc_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data if isinstance(data, dict) else {}
        except (json.JSONDecodeError, Exception):
            return {}
    else:
        return {}


def save_image_descriptions(folder_path: Path | str, descriptions: Dict[str, Any]) -> None:
    """
    Save image descriptions to JSON file in the specified folder.

    Args:
        folder_path: Path to the folder containing image_description.json
        descriptions: Dictionary with image descriptions to save
    """
    folder_path = Path(folder_path)
    desc_file = folder_path / "image_description.json"

    with open(desc_file, 'w', encoding='utf-8') as f:
        json.dump(descriptions, f, indent=2, ensure_ascii=False)


def process_images(
    folder_path: Path | str,
    keywords: Dict[str, Any],
    description_length: int = 200,
    main_keywords_key: str = "main_keywords",
    optional_keywords_key: str = "optional_keywords"
) -> Dict[str, Any]:
    """
    Process all image files in the specified folder and update image descriptions.

    Args:
        folder_path: Path to the folder containing images
        keywords: Dictionary of keywords loaded from load_keywords()
        description_length: Length of description string to set
        main_keywords_key: Key name for main keywords in keywords dict
        optional_keywords_key: Key name for optional keywords in keywords dict

    Returns:
        Updated image descriptions dictionary
    """
    folder_path = Path(folder_path)

    # Load existing image descriptions
    image_descriptions = load_image_descriptions(folder_path)

    # Collect all image files based on patterns from config
    image_files = []
    for pattern in Config.IMAGE_PATTERNS:
        image_files.extend(folder_path.glob(pattern))

    # Process each image file
    for image_file in image_files:
        # Get original filename
        original_filename = image_file.name

        # Extract image name (without extension and trailing numbers)
        image_name = extract_image_name(original_filename)

        # Sanitize filename to get new filename with extension
        sanitized_base = sanitize_filename(image_name)
        new_filename = f"{sanitized_base}{image_file.suffix}"

        # Look up keywords from the keywords dict
        keyword_data = keywords.get(image_name)

        if keyword_data is not None:
            # Extract main and optional keywords
            main_kws = keyword_data.get(main_keywords_key, [])
            optional_kws = keyword_data.get(optional_keywords_key, [])

            # Combine all keywords
            all_keywords = main_kws + optional_kws

            # Create description placeholder (string of specified length)
            description = "a" * description_length

            # Update image descriptions dict
            image_descriptions[new_filename] = {
                "image_name": image_name,
                "description": description,
                "description_length": len(description),
                "keywords": all_keywords,
                "count": len(all_keywords)
            }
        else:
            # No keywords found - set warning
            image_descriptions[new_filename] = {
                "image_name": image_name,
                "warning": f"No keywords found for: {image_name}",
                "description": "",
                "description_length": 0,
                "keywords": [],
                "count": 0
            }

    # Save updated descriptions back to file
    save_image_descriptions(folder_path, image_descriptions)

    return image_descriptions


def sanitize_filename_for_image(name: str) -> str:
    """
    Sanitize filename for microstock platforms.
    Similar to utils.sanitize_filename but preserves original case preferences.

    Args:
        name: Original filename base (without extension)

    Returns:
        Sanitized filename base
    """
    # Replace bad characters
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    # Replace multiple spaces with single underscore
    name = re.sub(r'\s+', '_', name.strip())
    # Convert to lowercase
    name = name.lower()

    # Truncate if too long
    if len(name) > Config.MAX_FILENAME_LENGTH:
        name = name[:Config.MAX_FILENAME_LENGTH]

    return name