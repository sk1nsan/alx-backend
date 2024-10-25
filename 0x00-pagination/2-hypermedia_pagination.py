#!/usr/bin/env python3

""" Hypermedia pagination """

from typing import Tuple, List, Dict, Any
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Simple helper function """
    start_idx = page_size * (page - 1)
    end_idx = page_size * page
    return (start_idx, end_idx)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ return pages selected """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_idx, end_idx = index_range(page, page_size)
        data = self.dataset()
        if (end_idx > len(data)):
            return []
        return data[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ returns a dictionary containing information about the data """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_idx, end_idx = index_range(page, page_size)
        data = self.dataset()
        n = len(data)
        total_pages = math.ceil(n / page_size)
        prev_page: Any = page - 1
        next_page: Any = page + 1
        if (end_idx > n):
            page_size = 0
            data = []
            next_page = None
        else:
            data = data[start_idx:end_idx]
        if (page <= 1):
            prev_page = None
        meta_data = {"page_size": page_size,
                     "page": page,
                     "data": data,
                     "next_page": next_page,
                     "prev_page": prev_page,
                     "total_pages": total_pages
                     }
        return meta_data
