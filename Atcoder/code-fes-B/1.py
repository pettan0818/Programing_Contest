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

def inputs():
    return input()

def check_wrong_strs(inputed):
    """

    >>> check_wrong_strs("C0DEFESTIVAL2O16")
    2
    >>> check_wrong_strs("FESTIVAL2016CODE")
    16
    """
    num = 0
    RIGHT = "CODEFESTIVAL2016"

    for i, n in zip(inputed, RIGHT):
        if i != n:
            num += 1
    return num



if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print(check_wrong_strs(inputs()))
