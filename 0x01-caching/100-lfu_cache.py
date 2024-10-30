#!/usr/bin/env python3

""" LFUCache """


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache """

    def __init__(self):
        """ init """
        super().__init__()
        self.pq = []

    def put(self, key, item):
        """ insert new item into the cache """
        pq = self.pq
        if not key or not item:
            return
        if (key in self.cache_data):
            for i in range(len(pq)):
                if pq[i][1] == key:
                    break
            updated_key = pq.pop(i)
            updated_key[0] += 1
            self.pq.append(updated_key)
            self.cache_data[key] = item
            return
        if (len(self.pq) >= BaseCaching.MAX_ITEMS):
            min = 0
            for i in range(len(pq)):
                if (pq[i][0] < pq[min][0]):
                    min = i
            deleted_item = self.pq.pop(min)
            del self.cache_data[deleted_item[1]]
            print(f"DISCARD: {deleted_item[1]}")
        pq.append([1, key])
        self.cache_data[key] = item

    def get(self, key):
        """ get item from cache """
        if key in self.cache_data:
            for i in range(len(self.pq)):
                if self.pq[i][1] == key:
                    break
            self.pq[i][0] += 1
        return self.cache_data.get(key)
