#!/usr/bin/env python3

"""
This is mixed tuple
"""

from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string `k` and a number `v` (which can be either an int or a float)
    and returns a tuple containing `k` and the square of `v`.

    Args:
        k (str): The string key.
        v (Union[int, float]): The number value.

    Returns:
        Tuple[str, float]: A tuple containing `k` and the square of `v`.
    """

    return (k, v * v)
