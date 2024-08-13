#!/usr/bin/env python3

"""
    List of floats
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of all elements in the input list.

    Args:
        input_list (str): The list of elements to be summed.

    Returns:
        float: The sum of all elements in the list.
    """

    return float(sum(input_list))
