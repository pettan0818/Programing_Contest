# -*- coding: utf-8 -*-
# !/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
#
# Author:   Noname
# URL:      https://github.com/pettan0818
# License:  MIT License
# Created: 火 11/ 8 16:49:06 2016

# Usage
#
"""
def read_input():
    N = int(input())
    K = int(input())
    X = int(input())
    Y = int(input())

    return N, K, X, Y


def check_sum(N, K, X, Y):
    """
    >>> check_sum(5, 3, 10000, 9000)
    48000
    >>> check_sum(2, 3, 10000, 9000)
    20000
    """
    if N > K:
        return K * X + (N-K)*Y
    else:
        return N * X


if __name__ == "__main__":
    # import doctest
    #
    # doctest.testmod()
    N, K, X, Y = read_input()

    check_sum(N, K, X, Y)
