#!/usr/bin/env python3
"""
This is a task
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute multiple coroutines concurrently and return their results.

    Args:
        n (int): Number of coroutines to run.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        List[float]: List of results from the coroutines, in the order
        they were completed.
    """

    tasks = []
    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    results = []
    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)

    return results