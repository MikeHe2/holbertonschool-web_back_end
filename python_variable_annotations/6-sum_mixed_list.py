#!/usr/bin/env python3

"""
This is a mixed list of ints and floats
"""
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a mixed list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing integers and floats.

    Returns:
        float: The sum of the elements in the mixed list.

    """

    return float(sum(mxd_lst))