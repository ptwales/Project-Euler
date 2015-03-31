args = (1, 1000)

def problem_1(lower, upper):
    
    def valid(n):
        return not ((x%5) and (x%3))
    
    return sum((n for n in xrange(lower, upper) if valid(n)))
