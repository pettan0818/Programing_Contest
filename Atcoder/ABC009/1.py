# -*- coding: utf-8 -*-
"""ABC 009 A Problem."""


def cal_time(num_of_cardboard: int) -> int:
    """Calc how many times he must work.

    >>> cal_time(1)
    1
    >>> cal_time(2)
    1
    >>> cal_time(5)
    3
    """
    return int(num_of_cardboard // 2 + num_of_cardboard % 2)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    num_of_cardboard = int(input())

    print(cal_time(num_of_cardboard))
