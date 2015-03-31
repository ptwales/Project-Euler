def is_even(n):
   return ((n % 2) == 0)

def tail(xs):
   return list(xs)[1::]

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
      
      def is_solved(n): 
         return n in sols
      
      result = []
      for c in cs:
         result.append(c)
         if is_solved(c):
            break
         
      return result
    
    
   def new_answers(nvs, sols):
      add_len = sols[nvs[-1]] # length of already solved collatz
      enum_nvs = enumerate(tail(reversed(nvs)))
      # swap the new values and add existing solution
      swapped = ((t[1], t[0] + add_len + 1) for t in enum_nvs) 
      return dict(swapped)
    
   def all_solutions(limit):    
      solutions = {1: 1}
      for n in range(2, limit):
         cs = collatz(n)
         nvs = new_values(cs, solutions)
         solutions.update(new_answers(nvs, solutions))
      return solutions

   solutions = all_solutions(limit)
    
   answers = {k: solutions[k] for k in range(1, limit)}
   return max(answers.iterkeys(), key=(lambda key: answers[key]))
