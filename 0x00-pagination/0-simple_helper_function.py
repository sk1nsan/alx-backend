#!/usr/bin/env python3

""" Simple helper function """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Simple helper function """
    start_idx = page_size * (page - 1)
    end_idx = page_size * page
    return (start_idx, end_idx)
