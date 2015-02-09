def is_even(n):
   return ((n % 2) == 0)


def collatz(n):
    yield n
    while n > 1:
        if is_even(n):
            n = n/2
        else:
            n = 3*n + 1
        yield n


def collatz_length(cs, sols):
    i = 0
    for n in cs:
        if n in sols:
            return i + sols[n]
        i += 1

    return n

    
def problem14(limit):
    
    sols = {1: 1}
    
    for n in range(2, limit):
        collatz_seq = collatz(n)
        sols[n] = collatz_length(collatz_seq, sols)
    
    return max(sols.iterkeys(), key=(lambda key: sols[key]))
