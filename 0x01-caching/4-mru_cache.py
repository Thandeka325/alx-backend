#!/usr/bin/env python3
"""
MRUCache module - a caching system that uses MRU replacement.
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache inherits from BaseCaching and implements
    a Most Recently Used (MRU) caching system.
    """

    def __init__(self):
        """Initialize the cache and usage tracking."""
        super().__init__()
        self.usage_order = []  # Keeps track of access order for MRU

    def put(self, key, item):
        """
        Add an item to the cache using MRU replacement policy.

        Args:
            key: The key to store the item under.
            item: The item to store.
        """
        if key is None or item is None:
            return

        # If key already exists, update its position
        if key in self.cache_data:
            self.usage_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Discard the most recently used key
            mru_key = self.usage_order.pop()  # Last used
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)

        # Add to cache and mark as most recently used
        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache and update usage order.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The cached item, or None if key is invalid or not found.
        """
        if key is None or key not in self.cache_data:
            return None

        # Update usage order: move key to end (most recently used)
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
