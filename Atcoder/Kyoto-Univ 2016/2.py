# -*- coding: utf-8 -*-
# !/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
#
# Author:   Noname
# URL:      https://github.com/pettan0818
# License:  MIT License
# Created:  2016-10-07
#

# Usage
#
"""
from collections import Counter

def read():
    """Read Problem as below.
    N K
    P_1
    P_2
    P_N
    """
    line1 = input().split(" ")
    num_of_problems = int(line1[0])
    per_kupc_problems = int(line1[1])

    names_of_problems = [input() for _ in range(num_of_problems)]

    return per_kupc_problems, names_of_problems

def initial_checker(names_of_problems):
    """Counter of Given Names.

    >>> initial_checker(["ABC", "ATP"])
    Counter({'A': 2})
    """
    initials = [a[0] for a in names_of_problems]
    count_initials = Counter(initials)

    return count_initials


def count_up_times_kucp(initial_counted_obj):
    """Count up how many times kucp can occur.
    >>> target = Counter(["A", "B", "C"])
    >>> count_up_times_kucp(target)
    1
    """
    variations = initial_counted_obj



if __name__ == "__main__":
    import doctest
    doctest.testmod()
