#!/usr/bin/env python3
"""Documenting module"""
from typing import List
from importlib import import_module as using

async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers from async_generator.

    Returns:
        A list of 10 random float numbers between 0 and 10.
    """
    return [num async for num in async_generator()]
