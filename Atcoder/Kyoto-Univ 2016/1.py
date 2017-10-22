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

def read():
    """Read like as below.
    N A B
    t_1
    t_n
    """
    line_1 = input().split(" ")
    num_of_class = int(line_1[0])
    blocked_class = line_1[1:2]
    blocked_class = range(int(line_1[1]), int(line_1[2]))

    following_class = {int(input()) for _ in range(num_of_class)}

    return following_class, blocked_class


def check_available_class(following_class, blocked_class):
    """Check how many class you can attend.
    >>> check_available_class([4,3,6,9,1], [5,6,7,8])
    4
    >>> check_available_class([5,6,7,8,9], [4,5,6,7,8])
    1
    """
    # return len(set(following_class).difference(blocked_class))
    attendable = [i for i in following_class if not i in blocked_class]
    return len(attendable)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    f, b = read()
    print(check_available_class(f,b))
