#!/usr/bin/env python3

""" Basic dictionary """

from queue import Queue

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache """

    def __init__(self):
        """ init """
        super().__init__()
        self.queue = Queue(BaseCaching.MAX_ITEMS)

    def put(self, key, item):
        """ insert new item into the cache """
        if not key or not item or key in self.cache_data:
            return
        if (self.queue.full()):
            deleted_item = self.queue.get()
            del self.cache_data[deleted_item]
            print(f"DISCARD: {deleted_item}")
        self.queue.put(key)
        self.cache_data[key] = item

    def get(self, key):
        """ get item from cache """
        return self.cache_data.get(key)
