args = (1, 21)


def gcd(a, b):
    """
    >>> gcd(1,1)
    1
    >>> gcd(45, 81)
    9
    """
    while b:      
        a, b = b, a % b
    return a



def lcm(a, b):
    """
    >>> lcm(1,1)
    1
    >>> lcm(3, 5)
    15
    """
    return a * b // gcd(a, b)


def lcmm(*a):
    return reduce(lcm, a)


def problem_5(lower, upper):
    return lcmm(*xrange(lower, upper))
