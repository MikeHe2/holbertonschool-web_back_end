#!/usr/bin/env python3

"""
This is a task
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> float:
    """
    Creates and returns a task that waits for a random amount of time.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: A task that waits for a random amount of time.
    """

    task = asyncio.create_task(wait_random(max_delay))
    return task
