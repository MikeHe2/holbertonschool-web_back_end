#!/usr/bin/env python3
"""
This is a task
"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(max_delay: int = 10, n: int = 0) -> float:
    """
    Measure the average time per coroutine for the function wait_n.

    Args:
        max_delay (int): Maximum delay for each coroutine.
        n (int): Number of coroutines to spawn.

    Returns:
        float: Average time per coroutine.
    """

    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    average_time = elapsed_time / n

    return average_time
