def read_input():
    return list(input())


def maximize_point(against):
    """Calc max point.

    >>> maximize_point(list("gpg"))
    0
    >>> maximize_point(list("ggppgggpgg"))
    2
    """
    cash = 0
    point = 0
    for hand in against:
        if hand == "g":
            if cash > 0:
                point += 1
                cash += -1
                # print("p")
            else:
                point += 0
                cash += 1
                # print("g")

        if hand == "p":
            if cash > 0:
                point += 0
                cash += -1
                # print("p")
            else:
                point += -1
                cash += 1
                # print("g")

    return point

if __name__ == "__main__":
    # import doctest

    # doctest.testmod()

    print(maximize_point(read_input()))
