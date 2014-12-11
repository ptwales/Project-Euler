LIMIT = 1000

def valid(n):
   return not ((x%5) and (x%3))

def problem_1(u):
    return sum((n for n in xrange(1, u) if valid(n)))

if __name__ == '__main__':
    print(problem_1(LIMIT))
