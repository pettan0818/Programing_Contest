# -*- coding: utf-8 -*-
# !/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
#
# Author:   Noname
# URL:      https://github.com/pettan0818
# License:  MIT License
# Created:  2016-10-10
#

# Usage
#
"""

def read_value():
    num_customer = int(input())

    return [int(input()) for _ in range(num_customer)]


def greed_canceler(customers):
    """

    >>> greed_canceler([3,2,5])
    3
    >>> greed_canceler([3,1,4,1,5,9,2,6,5,3,5,8,9,7,9])
    18
    """
    selled = 0
    must_above = 1
    for i, n in enumerate(customers):
        flag = False
        while must_above < customers[i]:
            flag = True
            selled += 1
            print("Processing col: {0} of {1}".format(i, customers[i]))
            customers[i] = customers[i] - must_above
            print("must_above: {0}".format(must_above))
            print(customers[i])
            last = customers[i]
        if must_above >= last:
            must_above = last + 1


    return selled

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    greed_canceler(read_value())
