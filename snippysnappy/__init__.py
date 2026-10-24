"""
Snippy Snappy

A collection of Cnosu's code snippets (basically a library)

Copyright Cnosu System 2026. GPLv3 license, see the LICENSE.md file.
"""

from .colors import Back, Fore, Reset, Style
from .ids import get_id
from .sorting import bubble_sort, optimized_bubble_sort

__version__ = "0.1.0"

__all__ = [
    "Back",
    "Fore",
    "Reset",
    "Style",
    "__version__",
    "bubble_sort",
    "get_id",
    "optimized_bubble_sort",
]
