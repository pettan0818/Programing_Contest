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

import itertools
import random
def read_input():
    line_1 = input().split()

    steps = int(line_1[0])
    head = int(line_1[1])

    return steps, head


def random_walk_fitter(steps, head):
    """
    >>> random_walk_fitter(4, 4)
    Yes
    >>> random_walk_fitter(2, 1)
    No
    """
    flag = True
    while flag is True:
        
