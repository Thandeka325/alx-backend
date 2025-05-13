#!/usr/bin/env python3
"""
LFUCache module - implements a caching system using LFU algorithm.
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache inherits from BaseCaching and implements a
    Least Frequently Used (LFU) cache system with LRU tiebreaker.
    """

    def __init__(self):
        """Initialize the cache and tracking dictionaries."""
        super().__init__()
        self.freq_count = {}     # Frequency of key usage
        self.usage_order = []    # Track access order for LRU

    def put(self, key, item):
        """
        Add an item using LFU + LRU caching policy.

        Args:
            key: The key to store the item under.
            item: The item to store.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq_count[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.freq_count.values())
                lfu_keys = [
                    k for k in self.cache_data
                    if self.freq_count[k] == min_freq
                ]

                if len(lfu_keys) > 1:
                    for k in self.usage_order:
                        if k in lfu_keys:
                            lfu_key = k
                            break
                else:
                    lfu_key = lfu_keys[0]

                del self.cache_data[lfu_key]
                del self.freq_count[lfu_key]
                self.usage_order.remove(lfu_key)
                print("DISCARD:", lfu_key)

            self.cache_data[key] = item
            self.freq_count[key] = 1
            self.usage_order.append(key)

    def get(self, key):
        """
        Retrieve item and update frequency and usage.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value if key exists, else None.
        """
        if key is None or key not in self.cache_data:
            return None

        self.freq_count[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
