args = (1, 21)

def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmm(*a):
    return reduce(lcm, a)

def problem_5(lower, upper):
    return lcmm(*xrange(lower, upper))
