# Generator_Comprehension_Performance
Generator_Comprehension Outperforms In all Looping Statements as well as Comprehensions such as List Comprehension!
<hr>

Generator Comprehensions are very similar to list comprehensions. 
One Difference between them is that generator comprehensions use 'circular brackets' whereas list comprehensions use 'square brackets'.

Major Difference between list and Generator Comprehension is that, Generators don't allocate memory for whole list. Instead, they generate each value one by one, which is why they are memory efficient!

<hr>

The Generator yields one item at a time and generates item only when in demand, Whereas in list comprehension, python reserves memory for the whole list.
Thus, we can say that generator expressions are memory efficient than list comprehensions!

# Using time module...
<img width="349" alt="image" src="https://user-images.githubusercontent.com/70468773/204124780-a8525b21-011b-4a81-9659-770f4cf9a505.png">
<hr>

# Using timeit module...
<img width="477" alt="image" src="https://user-images.githubusercontent.com/70468773/204124825-8ce4c425-735a-4a8c-8b53-d0262152de76.png">

# There is a remarkable difference in the execution time.
# Thus, generator expressions are faster than list comprehension and hence time efficient.

timeit module is far much efficient than time module in python


