#!/usr/bin/env python3

"""This is a task"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]: # type: ignore
    """
    Asynchronous generator that yields random floating-point numbers.

    Yields:
        float: A random floating-point number between 0 and 10.

    Raises:
s        None

    Returns:
        None
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
