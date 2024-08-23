#!/usr/bin/env python3

"""
contains an asynchronous function
"""

import asyncio
import bisect
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    asynchronously call the wait_random coroutine
    for n times
    """
    delay = []
    for n in range(0, n):
        wait = await wait_random(max_delay)
        bisect.insort(delay, wait)
    return delay
