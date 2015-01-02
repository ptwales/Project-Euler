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


# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/

def Eppstein_Sieve():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    composites_to_primes = {}  

    # The running integer that's checked for primeness
    n = 2  

    while True:
        if n not in composites_to_primes:
            # n is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            yield n        
            composites_to_primes[n * n] = [n]
        else:
            # n is composite. composites_to_primes[n] is the list of primes that
            # divide it. Since we've reached n, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            for p in composites_to_primes[n]:
                composites_to_primes.setdefault(p + n, []).append(p)
            del composites_to_primes[n]
        
        n += 1

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
