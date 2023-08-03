#!/usr/bin/env python3
"""This module defines a function `to_kv`"""
from typing import Union
from typing import Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns the sum of list elements"""
    return (k, v**2)
