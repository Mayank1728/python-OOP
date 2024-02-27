# Fibonacci series

"""
 Try to display like this
 0 1 1 2 3 5 8 13 21..
 also
 1 1 2 3 5...
"""

dict = {1: 1, 2: 1}
def fib(n):
 if(n <= 0):
  return 0
 if n in dict:
  return dict[n]
 dict[n] = fib(n-2) + fib(n-1)
 return dict[n]

 
ans = fib(25)
print(ans)







 
