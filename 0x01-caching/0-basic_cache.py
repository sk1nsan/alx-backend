#!/usr/bin/env python3

""" Basic dictionary """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache """

    def put(self, key, item):
        """ insert new item into the cache """
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ get item from cache """
        return self.cache_data.get(key)
