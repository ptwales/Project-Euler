import primes

def problem7(n):
    return primes.index_generator(primes.Eppstein_Sieve(), n-1)
