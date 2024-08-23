#!/usr/bin/env python3

"""
contains an asynchronous function
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    asynchronously call the wait_random coroutine
    for n times
    """
    delay = []
    for n in range(0, n):
        delay.append(await wait_random(max_delay))
    return sorted(delay)
