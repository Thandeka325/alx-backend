#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """
    Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Loads and caches dataset from CSV.
        Returns:
            List of dataset rows, excluding header.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Returns the dataset indexed by position.
        Returns:
            Dictionary where key is index and value is dataset row.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Deletion-resilient pagination:
        retrieves a page starting at index,
        skipping any deleted entries in the indexed dataset.

        Args:
            index (int): Starting index for the page.
            page_size (int): Number of items per page.

        Returns:
            Dict: Page data including index, next index, page size, and data.
        """
        assert index is not None and isinstance(index, int)
        assert 0 <= index < len(self.dataset())

        indexed_data = self.indexed_dataset()
        data = []
        current_index = index

        while len(data) < page_size and current_index < len(self.dataset()):
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
            current_index += 1

        return {
            'index': index,
            'next_index': current_index,
            'page_size': len(data),
            'data': data
        }
