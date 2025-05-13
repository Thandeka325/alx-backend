#!/usr/bin/env python3
"""
FIFOCache module - a caching system that uses FIFO replacement.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache inherits from BaseCaching and implements
    a FIFO caching system.
    """

    def __init__(self):
        """
        Initialize the cache and call the parent constructor.
        """
        super().__init__()
        self.order = []  # To track insertion order

    def put(self, key, item):
        """
        Add an item to the cache using FIFO replacement policy.

        Args:
            key: The key under which to store the item.
            item: The item to store.
        """
        if key is None or item is None:
            return

        # Removes existing key to avoid duplicates
        if key in self.cache_data:
            self.order.remove(key)

        self.cache_data[key] = item
        self.order.append(key)

        # Check if cache exceeds limit
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = self.order.pop(0)  # First-in key
            del self.cache_data[discarded_key]
            print("DISCARD:", discarded_key)

    def get(self, key):
        """
        Retrieve an item from the cache by key.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The cached item, or None if not found.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
