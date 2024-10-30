#!/usr/bin/env python3

""" Basic dictionary """


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache """

    def __init__(self):
        """ init """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ insert new item into the cache """
        if not key or not item:
            return
        if (key in self.cache_data):
            self.stack.remove(key)
            self.stack.append(key)
            return
        if (len(self.stack) >= BaseCaching.MAX_ITEMS):
            deleted_item = self.stack.pop()
            del self.cache_data[deleted_item]
            print(f"DISCARD: {deleted_item}")
        self.stack.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ get item from cache """
        return self.cache_data.get(key)
