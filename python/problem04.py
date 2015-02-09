args = (100, 1000)

def problem_4(lower, upper):

    def is_palindrome(x):
        return str(x) == str(x)[::-1]
    
    def permutate_pairs(S):
        for n, i in enumerate(S):
            for i2 in S[n::]:
                yield i*i2
                
    pairs = permutate_pairs(xrange(lower, upper))
    return(max(filter(is_palindrome, pairs)))
