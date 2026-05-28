import click
from .utils import sanitize_filename
from .config import Config

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

if __name__ == '__main__':
    main()