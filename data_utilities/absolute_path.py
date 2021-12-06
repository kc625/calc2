"""This functions helps us get the absolute path"""
from pathlib import Path

def absolutepath(filepath):
    """Turns a relative filepath into the absolute filepath"""
    relative = Path(filepath)
    return relative.absolute()
