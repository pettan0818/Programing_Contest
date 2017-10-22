# -*- coding: utf-8 -*-
# !/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
#
# Author:   Noname
# URL:      https://github.com/pettan0818
# License:  MIT License
# Created:  2016-10-27
#

# Usage
#
"""
from operator import mul
from functools import reduce

def get_input():
    line_1 = input().split()

    num = int(line_1[0])
    restriction = int(line_1[1])

    data = [int(input()) for _ in range(num)]

    return restriction, data


def naive_checker(restriction, data):
    """
    >>> naive_checker(6, [4,3,1,1,2,10,2])
    4
    >>> naive_checker(10, [10,10,10,10,0,10])
    6
    >>> naive_checker(9, [10,10])
    0
    >>> naive_checker(1, range(1,10))
    1
    >>> naive_checker(0, range(1,4))
    0
    >>> naive_checker(9, [10,10,10,10,10,10])
    0
    """
    if 0 in data:
        return len(data)
    potential = 0
    for i in range(0, len(data)):
        for r in range(potential, len(data)):
            if i + r > len(data):
                break
            if data[i+r-1] == 1:
                potential = r
            subset_data = data[i: i+r]
            # print(subset_data)
            if reduce(mul, subset_data, 1) > restriction:
                # print("over at ", potential)
                break
            if r > potential:
                potential = r
    return potential


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # re, da = get_input()
    #
    # print(naive_checker(re, da))
    #
