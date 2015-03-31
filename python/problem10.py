import primes

def problem10(limit):
    ps = itertools.takewhile(lambda x: x < limit, primes.Eppstein_Sieve())
    # ps = primes.Eratosthenes(limit) # memory error
    return sum(ps)
