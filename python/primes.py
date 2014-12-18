import itertools
import math


def fermats_little(n):
    """
    >>> fermats_little(2)
    True
    >>> fermats_little(16)
    False
    >>> fermats_little(61)
    True
    """
    
    for a in range(2, n):
        if (a**n) % n != a % n:
            return False
    return True



def naiive_is_prime(n):
    """
    >>> naiive_is_prime(2)
    True
    >>> naiive_is_prime(16)
    False
    >>> naiive_is_prime(61)
    True
    """
    def smallest_divisor(n):
        for i in range(2, int(math.ceil(n**0.5))):
            if n % i == 0:
                return i
        return n

    return (smallest_divisor(n) == n)

"""
"""
def infinite_primes(is_prime):
    for n in itertools.count(2):
        if is_prime(n):
            yield n
 

def index_generator(gen, i):
    """
    >>> index_generator(itertools.count(), 42)
    42
    """
    return next(itertools.islice(gen, i, i+1))
