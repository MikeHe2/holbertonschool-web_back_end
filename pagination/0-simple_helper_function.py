#!/usr/bin/env python3

"""This is a task"""

from typing import Tuple

def index_range(page , page_size) -> Tuple[int, int]:

    final_index = page * page_size
    start_index = final_index - page_size

    return start_index, final_index