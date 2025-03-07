#!/usr/bin/env python3
"""Documenting module"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Asynchronously generates 10 random numbers between 0 and 10.

    Yields:
        A random float number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
