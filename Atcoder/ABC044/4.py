# -*- coding: utf-8 -*-
# !/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
#
# Author:   Noname
# URL:      https://github.com/pettan0818
# License:  MIT License
# Created: 火 11/ 8 17:18:36 2016

# Usage
#
"""
def read_input():
    n = int(input())
    s = int(input())

    return n, s


def naive_transform(n, b):
    """
    >>> naive_transform(87654, 10)
    30
    >>> naive_transform(87654, 100)
    138
    """
    sumof = 0
    while n > b:
        sumof += n % b
        n = n // b
    sumof += n
    return sumof


def check_existance(n, s):
    """
    >>> check_existance(87654, 30)
    10
    """
    for b in range(1, n):
        temp = naive_transform(n, b)
        print(b)
        if s == temp:
            print(b)
        if s < temp:
            print(-1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
