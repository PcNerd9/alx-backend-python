#!/usr/bin/env python3
"""
contains an asynchronous function
"""

import asyncio
import bisect
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    asynchronously call the wait_random coroutine
    for n times
    """
    delay = []
    for n in range(0, n):
        task = task_wait_random(max_delay)
        wait = await task
        bisect.insort(delay, wait)
    return delay
