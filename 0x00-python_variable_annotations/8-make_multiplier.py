#!/usr/bin/env python3
"""Documenting Module"""

# 8-make_multiplier.py
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return lambda x: x * multiplier
