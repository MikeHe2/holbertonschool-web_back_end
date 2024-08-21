#!/usr/bin/env python3

"""This is a task"""

from typing import Tuple

def index_range(page , page_size) -> Tuple[int, int]:
    """
    Returns the start and final index of a given page and page size.

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and final index of the page.
    """

    final_index = page * page_size
    start_index = final_index - page_size

    return start_index, final_index
