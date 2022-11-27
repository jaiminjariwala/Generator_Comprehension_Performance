
import time

# using for loop
def for_loop(n):
    result = []
    for i in range(n):
        result.append(i**2)
    return result

# using list comprehension
def list_comprehension(n):
    return [i**2 for i in range(n)]

# using generator comprehension
def generator_comprehension(n):
    return (i**2 for i in range(n))

# calculating time taken by for_loop
begin = time.time()
for_loop(10**6)
end = time.time()
print("Time taken by for_loop: ", round(end-begin, 3))

# calculating time taken by list comprehension
begin = time.time()
list_comprehension(10**6)
end = time.time()
print("Time taken by list_comprehension: ", round(end-begin, 3))

# calculating time taken by generator comprehension
begin = time.time()
generator_comprehension(10**6)
end=time.time()
print("Time taken by generator_comprehension: ", (end-begin))

# doubt in generator comprehension time complexity(solved in Generator_Comprehension.py) file by using timeit module