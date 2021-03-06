import itertools
import math

# TODO
def Fermats_little(n):
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


def infinite_primes(is_prime):
    """
    """
    for n in itertools.count(2):
        if is_prime(n):
            yield n


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
    
    # (composite number) => [prime factors]
    composite_to_primes = {}  

    for n in itertools.count(2):
        if n not in composite_to_primes:
            # n is not composite -> it is prime
            yield n 
            # n * n is composite and it's only prime factors are [n]
            composite_to_primes[n * n] = [n]
        else:
            # composite + prime -> composite?
            for prime in composite_to_primes[n]:
                composite_to_primes.setdefault(prime + n, []).append(prime)
            del composite_to_primes[n]


def some_sieve(n):
    
    limit = int(n ** 0.5) + 1 # only need to operate to limit
    work = range(2, limit) # we will run the sieve to the limit
    rest = range(limit, n) # the rest is free
    composites = set() # mutable set to remember composites
    
    for i in work:
        if i not in composites:
<<<<<<< HEAD
            yield i # i is a prime
            # forget all composites below i
            past_composites = set(filter(lambda x: x < i, composites))
            composites -= past_composites
            # all multiples of i up to n are composite
            new_composites = set(range(i + i, n + 1, i))
            composites |= new_composites

    for i in (set(rest) - composites):
        yield i # free primes
=======
            yield i
            composites.update(range(i + i, n + 1, i))
            # TODO: remove everything under i from composites
    
    for i in set(rest).difference(composites):
        yield i


def Eratosthenes(limit):
>>>>>>> master
    
    domain = range(2, limit)
    primes_array = [True for i in domain]

    for n in domain:
        if primes_array[n]:
            yield n
            for i in xrange(n, limit, n):
                primes_array[i] = False
 

def index_generator(gen, i):
    """
    >>> index_generator(itertools.count(), 42)
    42
    """
    return next(itertools.islice(gen, i, i+1))
