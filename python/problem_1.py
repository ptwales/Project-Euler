args = (1000)

def problem_1(u):
    
    def valid(n):
        return not ((x%5) and (x%3))
    
    return sum((n for n in xrange(1, u) if valid(n)))
