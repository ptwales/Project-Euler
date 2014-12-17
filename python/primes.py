import itertools
import math

"""
>>> fermats_little(2)
True
>>> fermats_little(16)
False
>>> fermats_little(61)
True
"""
def fermats_little(n):
    for a in xrange(2, n):
        if (a**n) % n != a % n:
            return False
    return True


"""
>>> naiive_is_prime(2)
True
>>> naiive_is_prime(16)
False
>>> naiive_is_prime(61)
True
"""
def naiive_is_prime(n):
    
    def smallest_divisor(n):
        for i in xrange(2, int(math.ceil(n**0.5))):
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
 
"""
>>> index_generator(itertools.count(), 42)
42
"""
def index_genertor(gen, i):
     return itertools.islice(gen, i-1, i).next()
