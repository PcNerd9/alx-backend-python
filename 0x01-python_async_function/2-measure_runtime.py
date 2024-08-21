#!/usr/bin/env python3

"""
contains an asynchronous coroutine
"""
import asyncio
from time import perf_counter
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n, max_delay):
    if n <= 0:
        return -1
    before = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    after = perf_counter()
    return (after - before) / n
