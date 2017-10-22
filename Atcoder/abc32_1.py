def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
        return a * b // gcd (a, b)

def get_input():
    a = int(input())
    b = int(input())
    n = int(input())

    return a, b, n

def like_num(a, b, n):
    """
    >>> like_num(2,3,8)
    12
    """
    potential = lcm(a,b)
    result = potential
    while result < n:
        result += potential

    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    a,b,n = get_input()
    print(like_num(a,b,n))
