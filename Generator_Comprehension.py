
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
