# -*- coding: utf-8 -*-
# !/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
#
# Author:   Noname
# URL:      https://github.com/pettan0818
# License:  MIT License
# Created:  2016-09-28
#

# Usage
#
"""
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import

def input_process():
    """Receive Inputs."""
    return input()


def insert_space(target_str: str) -> str:
    """
    >>> insert_space("codefestival")
    code festival
    """
    return target_str[0:4] + " " + target_str[4:]

if __name__ == "__main__":
    target = input()

    print(insert_space(target))
