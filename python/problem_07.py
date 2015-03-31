import primes

def problem_7(n):
    """
    >>> problem_7(6)
    13
    """
    return primes.index_generator(primes.Eppstein_Sieve(), n-1)
    
    
