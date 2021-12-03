"""Function to get absolute path"""
from pathlib import Path

def absolutepath(filepath):
    """Returns the absolute path from the relative path"""
    relative = Path(filepath)
    return relative.absolute()