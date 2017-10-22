# -*- coding: utf-8 -*-
# !/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
#
# Author:   Noname
# URL:      https://github.com/pettan0818
# License:  MIT License
# Created: 日 10/22 22:40:49 2017

# Usage
#
"""
def checker(target: str):
    return "".join(reversed(target)) == target

if __name__ == '__main__':
    import doctest
    doctest.testmod()
