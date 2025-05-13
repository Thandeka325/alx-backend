#!/usr/bin/env python3
"""
LRUCache module - a caching system that uses LRU replacement.
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache inherits from BaseCaching and implements
    a Least Recently Used (LRU) caching system.
    """

    def __init__(self):
        """Initialize the cache and usage tracking."""
        super().__init__()
        self.usage_order = []  # Keeps track of access order for LRU

    def put(self, key, item):
        """
        Add an item to the cache using LRU replacement policy.

        Args:
            key: The key to store the item under.
            item: The item to store.
        """
        if key is None or item is None:
            return

        # If key already exists, remove it to reinsert and update usage order
        if key in self.cache_data:
            self.usage_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Evict least recently used
            lru_key = self.usage_order.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)

        # Add to cache and update usage order
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

        # Update usage order: move accessed key to the end
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
