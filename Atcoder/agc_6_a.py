# -*- coding: utf-8 -*-
# !/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
#
# Author:   Noname
# URL:      https://github.com/pettan0818
# License:  MIT License
# Created:  2016-10-29
#

# Usage
#
"""
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import

def read_input():
    min_len = int(input())
    first_str = list(input())
    end_str = list(input())

    return min_len, first_str, end_str


def check_dup(first_str, end_str, min_len):
    """

    >>> check_dup("expr", "expr", 4)
    4
    >>> check_dup("a", "z", 1)
    2
    >>> check_dup("abc", "cde", 3)
    5
    >>> check_dup("expr", "expr", 5)
    8
    """
    for char_num in range(len(end_str), 0, -1):
        sub_f = first_str[char_num * -1:]
        sub_e = end_str[: char_num]

        if sub_f == sub_e:
            result = len(sub_f) + (len(end_str) - char_num) * 2
            if result < min_len:
                continue
            else:
                return result

    return len(first_str) + len(end_str)



if __name__ == "__main__":
    import doctest
    doctest.testmod()

    min_len, f, e = read_input()

    print(check_dup(f, e, min_len))
