# sqrt(a**2 + b**2) + a + b = 1000
# a < b
def sqr(x):
    return x ** 2

def is_int(x):
    return float(x).is_integer()

def problem9(x):
    
    sqrx = sqr(x)
    
    def fb(a):
        return (sqrx - 2*x*a)/(2*(x - a))
    
    def fc(a, b):
        return (sqr(a) + sqr(b)) ** 0.5
    
    for a in range(1, x/3 + 1):
        b = fb(a)
        if is_int(b):
            c = fc(a, b)
            if is_int(c):
                return (a * b * c)

