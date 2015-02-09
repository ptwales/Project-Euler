from itertools import takewhile

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

    
def problem14(limit):
    
    def new_values(cs, sols):
        def is_new_value(n): n not in sols
        return [n for n in takewhile(cs, is_new_value)]
    
    def new_answers(nvs, sols):
        add_len = sols[nvs[-1]] # length of already solved collatz
        enum_nvs = list(enumerate(nvs)).reverse()[1::] # the new values enumerated
        # swap the new values and add existing solution
        swapped = ((t[1], t[0] + add_len) for t in enum_nvs) 
        return dict(swapped)
        
    answers = {1: 1}
    for n in range(2, limit):
        cs = collatz(n)
        nvs = new_values(cs, answers)
        answers[n] += new_answers(nvs, answers)
    
    return max(answers.iterkeys(), key=(lambda key: answers[key]))
