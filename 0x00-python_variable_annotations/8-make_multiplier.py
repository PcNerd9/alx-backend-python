#!/usr/bin/env python3

"""
contains a function that returns a callable
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    return a function
    """
    def function(v: float, mulitplier: float = multiplier) -> float:
        """
        return multiplication of float
        """
        return multiplier * v

    return function
