#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int, page_size: int = 10) -> Dict:
        """Returns a dictionary containing information about the data
        """
        total_data = self.indexed_dataset()
        n = len(total_data)
        next_index = None
        selected_data = []
        i = index
        j = page_size

        assert n >= index

        while n >= i:
            if (i not in total_data):
                i += 1
                continue
            selected_data.append(total_data[i])
            j -= 1
            i += 1
            if (not j):
                next_index = i
                break
        meta_data = {"index": index,
                     "data": selected_data,
                     "page_size": page_size,
                     "next_index": next_index
                     }
        return meta_data
