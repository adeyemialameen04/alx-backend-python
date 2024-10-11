#!/usr/bin/env python3
"""Documenting Module"""

# 100-safe_first_element.py
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
