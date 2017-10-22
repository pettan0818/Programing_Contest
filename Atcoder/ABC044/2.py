# vim: fileencoding=utf-8

from collections import Counter

def read_input():
    return input()

def check_beauty(s):
    """
    >>> check_beauty("abaccaba")
    Yes
    >>> check_beauty("hthth")
    No
    """
    checker = Counter(s)
    checker_key = [i[1] for i in checker.items() if not i[1] % 2 == 0]

    if len(checker_key) > 0:
        print("No")
    else:
        print("Yes")


if __name__ == '__main__':

    # import doctest
    #
    # doctest.testmod()

    s = read_input()

    check_beauty(s)
