# sqrt(a**2 + b**2) + a + b = 1000
# a < b
import math

for b in xrange(1, 1000):
    for a in xrange(1, b):
        c = (a**2 + b**2) ** (0.5)
        if a+b+c == 1000:
            c = int(c)
            print("a=%i, b=%i, c=%i" % (a, b, c))
            print("a+b+c=%i" % (a+b+c))
            print("abc=%i" % (a*b*c))
            exit()
