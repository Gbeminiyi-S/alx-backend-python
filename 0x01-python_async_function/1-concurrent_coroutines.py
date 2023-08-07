#!/usr/bin/env python3
"""This module defines the function `wait_n`"""
import asyncio
import random


wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n, max_delay):
    tasks = [wait_random(max_delay) for _ in range(n)]

    results = await asyncio.gather(*tasks)
    
    return sorted(results)
