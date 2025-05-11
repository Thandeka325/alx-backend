#!/usr/bin/env python3
"""
This module provides a helper function to calculate,
index ranges for pagination.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of start and end indexes for pagination

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple ( start index, end index).
    """
    start: int = (page - 1) * page_size
    end: int = page * page_size
    return start, end
