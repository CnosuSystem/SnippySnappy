"""
Snippy Snappy

A collection of Cnosu's code snippets (basically a library)

Copyright Cnosu System 2026. GPLv3 license, see the LICENSE.md file.
"""

from .colors import Back, Fore, Reset, Style
from .ids import get_id

__version__ = "0.1.0"

__all__ = ["Back", "Fore", "Reset", "Style", "__version__", "get_id"]
