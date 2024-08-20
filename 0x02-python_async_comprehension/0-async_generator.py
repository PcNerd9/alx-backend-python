#!/usr/bin/env python3

"""
contains asynchronous function
"""

import asyncio
from random import uniform


async def async_generator():
    """
    an async generator that yeilds
    a value from 0 to 10 randomly
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
