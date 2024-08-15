#!/usr/bin/env python3

"""
contains a function that returns a callable
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def function(v: float, mulitplier: float = multiplier) -> float:
        return multiplier * v

    return function
