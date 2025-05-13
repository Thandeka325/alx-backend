#!/usr/bin/env python3
"""
LIFOCache module - a caching system that uses LIFO replacement.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache inherits from BaseCaching and implements
    a LIFO caching system.
    """

    def __init__(self):
        """
        Initialize the cache and call the parent constructor.
        """
        super().__init__()
        self.last_key = None  # Track the last key inserted

    def put(self, key, item):
        """
        Add an item to the cache using LIFO replacement policy.

        Args:
            key: The key under which to store the item.
            item: The item to store.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        # If cache exceeds the limit
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.last_key in self.cache_data:
                del self.cache_data[self.last_key]
                print("DISCARD:", self.last_key)

        self.last_key = key  # Update last inserted key

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
