#!/usr/bin/env python3

"""
contain an asynchronous function that
wait for a random amount of time
"""

import asyncio
from random import uniform


async def wait_random(max_delay = 10):
    """
    wait for a random amount of time
    asynchronously
    """
    wait_time = uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
