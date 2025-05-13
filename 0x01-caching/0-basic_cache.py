#!/usr/bin/env python3
"""
0-basic_cache.py

BasicCache module - a simple caching system with no limit.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache inherits from BaseCaching and implements
    a simple dictionary-based caching system with no limit.
    """

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key under which to store the item.
            item: The item to store.

        Returns:
            None
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

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
