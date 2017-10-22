# -*- coding: utf-8 -*-
"""ABC 009 B Problem."""


def read_lines():
    # _ = stdin.read()
    # each_cost = stdin.readline().split("\n").pop()
    num_of_menu = int(input())
    each_cost = [input() for _ in range(num_of_menu)]

    return each_cost


def choose_second_highest(cost_list: list) -> int:
    """Choose 2nd highest Menu.

    >>> choose_second_highest([100,200,200])
    100
    >>> choose_second_highest([100, 200, 300, 300])
    200
    >>> choose_second_highest([50, 370, 819, 433, 120])
    433
    """
    inted_cost_list = [int(i) for i in cost_list]
    cost_list_wihtout_dup = list(set(inted_cost_list))

    return sorted(cost_list_wihtout_dup)[-2]


if __name__ == "__main__":
    print(choose_second_highest(read_lines()))
