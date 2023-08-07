#!/usr/bin/env python3
"""This module defines the function `wait_random`"""
import asyncio
import random


async def wait_random(max_delay=10):
    """ Asynchronous coroutine that waits for a random delay
        and eventually returns it
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay