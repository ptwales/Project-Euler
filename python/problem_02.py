args = (4 * 10**6, )

def problem_2(limit):

    def fib(n):
        a, b = 0, 1
        while a < n:
            a, b = b, a + b
            yield a
            
    return sum((x for x in fib(limit) if not x % 2))
