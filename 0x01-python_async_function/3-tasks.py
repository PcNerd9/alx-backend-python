#!/usr/bin/env python3

"""
contain an asynchronous function
"""

import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    return an asyncrohous task that is been scheduled
    by the event handler
    """
    return asyncio.create_task(wait_random())
