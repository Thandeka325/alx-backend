#!/usr/bin/env python3
"""
This module provides a Server class that paginates,
a dataset of popular baby names.
"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of start and end indexes for pagination params.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple (start index, end index).
    """
    start: int = (page - 1) * page_size
    end: int = page * page_size
    return start, end


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initializes the server and sets dataset cache to None."""
        self.__dataset = None

    def dataset(self) -> List[List[str]]:
        """
        Loads and caches the dataset from a CSV file.

        Returns:
            List[List[str]]: The dataset excluding the header.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Returns a page of the dataset corresponding to the
        pagination parameters.

        Args:
            page (int): The page number to retrieve (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List[str]]: A sublist of the dataset for the requested page.

        Raises:
            AssertionError: If page or page_size is not a positive integer.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        return dataset[start:end]
