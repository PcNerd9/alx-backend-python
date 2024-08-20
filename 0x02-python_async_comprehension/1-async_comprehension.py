#!/usr/bin/env python3

"""
contain asynchronous list comprehension
"""

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    return a list of random floats using list comprehension
    """
    return [value async for value in async_generator()]
