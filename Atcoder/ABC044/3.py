# -*- coding: utf-8 -*-
# !/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
#
# Author:   Noname
# URL:      https://github.com/pettan0818
# License:  MIT License
# Created: 火 11/ 8 17:04:53 2016

# Usage
#
"""

from itertools import repeat  # NOQA
from itertools import combinations

from statistics import mean


def read_input():
    first = input().split(" ")
    N = int(first[0])
    A = int(first[1])

    x_list = [int(i) for i in input().split(" ")]

    return N, A, x_list


def naive_checker(num_list, target_mean):
    """
    >>> naive_checker([7,9,8,9], 8)
    5
    >>> naive_checker([6,6,9], 8)
    0
    >>> naive_checker([3,6,2,8,7,6,5,9], 5)
    19
    >>> naive_checker(repeat(3,33), 3)
    8589934591
    """
    ans = 0
    for i in range(1, len(num_list) + 1):
        for n in combinations(num_list, i):
            if mean(n) == target_mean:
                ans += 1
    print(ans)


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()

    N, A, x_list = read_input()

    naive_checker(x_list, A)
