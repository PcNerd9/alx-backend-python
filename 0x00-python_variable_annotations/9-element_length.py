#!/usr/bin/env python3

"""
contains a function that returns a list of tuple
"""
from typing import List, Iterator, Sequence, Tuple


def element_length(lst: Iterator[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
