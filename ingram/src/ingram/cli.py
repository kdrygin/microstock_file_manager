import click
from pathlib import Path
from .utils import sanitize_filename
from .config import Config
from .keywords import load_keywords
from .image_processor import process_images, load_image_descriptions

@click.group()
def main():
    """Ingram - Microstock File Manager"""
    pass

@main.command()
@click.argument('filepath')
@click.option('--title', '-t', help='Title for the file')
def rename(filepath, title):
    """Rename file using microstock rules"""
    path = Path(filepath)
    if not path.exists():
        click.echo("File not found!")
        return

    clean_name = sanitize_filename(title or path.stem)
    new_name = f"{clean_name}{path.suffix}"
    new_path = path.parent / new_name

    path.rename(new_path)
    click.echo(f"Renamed: {new_name}")

@main.command()
@click.argument('folder', type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.option('--description-length', '-l', default=200, help='Length of description string')
def process(folder, description_length):
    """Process images in folder and update image_description.json"""
    folder_path = Path(folder)

    # Load keywords
    try:
        keywords = load_keywords()
    except FileNotFoundError as e:
        click.echo(f"Error: {e}")
        return
    except Exception as e:
        click.echo(f"Error loading keywords: {e}")
        return

    # Process images
    click.echo(f"Processing images in {folder_path}...")
    result = process_images(
        folder_path=folder_path,
        keywords=keywords,
        description_length=description_length
    )

    click.echo(f"Processed {len(result)} images.")
    click.echo(f"Descriptions saved to {folder_path / 'image_description.json'}")


@main.command()
def run():
    print('test')
    keywords = load_keywords()
    print(keywords['Happy parents and baby with birthday cake'])

if __name__ == '__main__':
    main()