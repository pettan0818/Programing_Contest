class SquareFreeString(object):
    def isSquareFree(self, s):
        """
        >>> tester = SquareFreeString()
        >>> tester.isSquareFree("bobo")
        not square-free
        >>> tester.isSquareFree("pen")
        square-free
        >>> tester.isSquareFree("apple")
        not square-free
        >>> tester.isSquareFree("qwertyuiopasdfghjklzxcvbnm")
        square-free
        """
        test = set(s)
        if len(s) == len(test):
            print("square-free")
        else:
            print("not square-free")
