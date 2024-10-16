#!/usr/bin/env python3
"""Documenting module"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Asynchronously generates 10 random numbers between 0 and 10.

    Yields:
        A random float number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
