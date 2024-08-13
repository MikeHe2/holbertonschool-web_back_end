#!/usr/bin/env python3
"""
This is task
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a given number by the specified multiplier.

    Args:
        multiplier (float): The multiplier to be used for multiplication.

    Returns:
        Callable[[float], float]: A function that takes a float as input and returns the result of multiplying it by the multiplier.
    """

    def multiply(num: float) -> float:
        return num * multiplier

    return multiply
