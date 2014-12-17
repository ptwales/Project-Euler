import itertools

def fermats_little(n):
    for a in xrange(2, n):
        if (a**n) % n != a % n:
            return False
    return True


def naiive_is_prime(n):
    
    def smallest_divisor(n):
        i = 0
       while True:
            if i**2 > n:
                return n
            elif n % i == 0:
                return i
            else
                i += 1
                
    return (smallest_divisor(n) == n)


def infinite_primes(is_prime):
    for n in itertools.count(2):
        if is_prime(n):
            yield n
 

def index_genertor(gen, i):
     return itertools.islice(gen, i-1, i).next()
