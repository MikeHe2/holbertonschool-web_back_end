#!/usr/bin/env python3

"""
This is a task
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in a list.
    Args:
        lst (Iterable[Sequence]): The list of elements.
    Returns:
        List[Tuple[Sequence, int]]: A list of tuples containing
        each element and its length.
    """

    return [(i, len(i)) for i in lst]
