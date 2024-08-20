#!/usr/bin/env python3

"""
contains asynchronous funtion
"""

import asyncio
from time import perf_counter
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime():
    """
    asynchronously run the async_comprehension funtion
    for four time
    """
    before = perf_counter()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         )
    after = perf_counter()
    return after - before
