class ThueMorseGame(object):
    def get(self, n, m):
        """
        >>> tester = ThueMorseGame()
        >>> tester.get(3,3)
        "Alice"
        >>> tester.get(3,2)
        "Bob"
        >>> tester.get(387, 22)
        "Alice"
        >>> tester.get(49999999, 50)
        "Alice"
        >>> tester.get(499999975, 49)
        "Alice"
        """

def num_checker(num):
    """
    >>> tester = ThueMorseGame()
    >>> tester.num_checker(3)
    True
    >>> tester.num_checker(19)
    False
    """
    if bin(num).count("1") % 2 == 0:
        return True
    else:
        return False
