args = (1, 100)

"""
>>> gauss_sum(1, 10)
55
>>> gauss_sum(5, 10)
40
"""
def gauss_sum(lo, hi):

    def from_one(n):
        return n*(n + 1)/2
    
    return from_one(hi) - from_one(lo - 1)

"""
>>> gauss_sqrsum(1, 10)
385
"""
def gauss_sqrsum(lo, hi):

    def from_one(n):
        return n*(2*n+1)*(n+1)/6
    
    return from_one(hi) - from_one(lo - 1)
    
"""
>>> problem_6(1, 10)
2640
"""
def problem_6(lo, hi):
    
    def from_one(n):
        return  n*(n**3 / 4 + n**2 / 6 - n/4 - 1)
    
    return from_one(hi) - from_one(lo - 1)
