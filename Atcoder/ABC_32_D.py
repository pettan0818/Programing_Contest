"""ナップザック問題〜深さ優先探索"""
import functools


def read_input():
    line_1 = input().split(" ")
    knapsack = int(line_1[1])

    baggage_info = [n.split(" ") for n in input()]
    baggage_info = [[int(i) for i in n] for n in baggage_info]

    return knapsack, baggage_info


def explorer():
    """深さ優先探索再帰関数

    >>> explorer()

    >>> explorer()
    """

