#!/usr/bin/env python3

"""
contains a function that returns a list of tuple
"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    return a list of a tuple
    """
    return [(i, len(i)) for i in lst]
