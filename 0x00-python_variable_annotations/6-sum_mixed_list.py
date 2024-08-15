#!/usr/bin/env python3

"""
contains a function that returns the sum of all
the elements in a list
"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """
    return the sum of all the elements of a list
    """
    return sum(mxd_lst)
