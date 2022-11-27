# Reference: GFG.Comprehensions_in_python.Generator_Comprehension

# Generator Comprehensions are very similar to list comprehensions.
# One Difference between them is that generator comprehensions use 'circular brackets'
# whereas list comprehensions use 'square brackets'.

# Major Difference between list and Generator Comprehension is that, Generators don't allocate memory for whole list.
# Instead, they generate each value one by one, which is why they are memory efficient

# --------------------IMP---------------------------
# When a normal function with a return statement is called, it terminates whenever it gets the return statement.
# But a function with a yield statement, saves the state of the function and can be picked up from the same state, next time the function is called.
# The Generator Expression allows us to create a generator without the yield keyword

# Difference between Generator Expressions and List Comprehensions?
# The Generator yields one item at a time and generates item only when in demand.
# Whereas in list comprehension, python reserves memory for the whole list.
# Thus, we can say that generator expressions are memory efficient than list comprehensions!

print()
from sys import getsizeof

list_comp = [i for i in range(10_000)]
gen = (i for i in range(10_000))

# gives size for list comprehension
x = getsizeof(list_comp)
print("Size taken by List Comprehension in memory is:", x)

# gives size for generator comprehension / generator expression
y = getsizeof(gen)
print("Size taken by Generator Comprehension in Memory is:", y)

# Hence Generator Expressions are space Efficient, proved!

print("------------------------------------------------------------------------------------")

# Let's check whether they are time efficient or not?

import timeit

print("Time taken by List Comprehension is:", timeit.timeit(stmt = '''list_comp = [i for i in range(100) if i % 2 == 0]''', number = 1_000_000))

print("Time taken by Generator Comprehension is:", timeit.timeit(stmt = '''gen = (i for i in range(100) if i % 2 == 0)''', number=1_000_000))

# There is a remarkable difference in the execution time.
# Thus, generator expressions are faster than list comprehension and hence time efficient.

# timeit module is far much efficient than time module in python

# More about the timeit module on GFG.timeit_module_python