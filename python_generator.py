#-------------------
# Python Generator
#-------------------

# Idea behind generator :
# There is a lot of work in building an iterator in Python. We have to implement a class with __iter__() and __next__() method,
# keep track of internal states, and raise StopIteration when there are no values to be returned.

# This is both lengthy and counterintuitive. Generator comes to the rescue in such situations.

# Python generators are a simple way of creating iterators. All the work we mentioned above are automatically handled by generators in Python.
# Simply speaking, a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).


#------------------------------------------------------------------------------------------------------------
# Example 1 : Create Generators in Python
#             It is fairly simple to create a generator in Python.
#             It is as easy as defining a normal function, but with a yield statement instead of a return statement.
#             NOTE : The difference is that while a return statement terminates a function entirely,
#                    yield statement pauses the function saving all its states and later continues from there on successive calls.

# Difference between Generator function and Normal function :
#   1. Generator function contains one or more yield statements.
#   2. When called, it returns an object (iterator) but does not start execution immediately.
#   3. Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().
#   4. Once the function yields, the function is paused and the control is transferred to the caller.
#   5. Local variables and their states are remembered between successive calls.
#   6. Finally, when the function terminates, StopIteration is raised automatically on further calls.

# Here we have a generator function named my_gen() with several yield statements.

print("\n")

def my_gen():
    n = 55

    print("This is printed first")
    yield n  # when next() is call for the first time, the function will halt after yield n

    n += 1
    print("This is printed second")
    yield n  # when next() is call for the second time, the function will halt after yield n

    n += 1
    print("This is printed third")
    yield n

a = my_gen()

print(next(a))
print(next(a))
print(next(a))

# next(a) # UNCOMMENT TO RUN : This will generate an exception as end of iterator has been reached : StopIteration

# One interesting thing to note in the above example is that the value of variable n is remembered between each call.
# Unlike normal functions, the local variables are not destroyed when the function yields. Furthermore, the generator object can be iterated only once.
# NOTE : To restart the process we need to create another generator object using something like a = my_gen().
# NOTE : One final thing to note is that we can use generators with for loops directly (check Example 2).

#------------------------------------------------------------------------------------------------------------
# Example 2 : Using generators with for loops

print("\n")

for item in my_gen():
    print(item)

# A more useful example
def str_reverse(str): # small function of reversing a string using yield
    for i in range(len(str)-1, -1, -1):
        yield str[i]

for i in str_reverse("jayant"):
    print(i, end=" ")

#------------------------------------------------------------------------------------------------------------
# Example 3 : Python Generator Expression
#             Simple generators can be easily created on the fly using generator expressions. It makes building generators easy.
#             NOTE : Similar to the lambda functions which create anonymous functions, generator expressions create anonymous generator functions.
#             syntax : The syntax for generator expression is similar to that of a list comprehension in Python.
#                      But the square brackets are replaced with round parentheses.
#
#                      The major difference between a list comprehension and a generator expression is that
#                      a list comprehension produces the entire list while the generator expression produces one item at a time.

print("\n")

my_list = [1, 2, 3, 4]

# square each term using list comprehension
list_ = [x**2 for x in my_list]

# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
generator_func1 = (x**2 for x in my_list)

print(list_)
print(generator_func1)  # This will return an iterator object

print(next(generator_func1))
print(next(generator_func1))
print(next(generator_func1))
print(next(generator_func1))
#print(next(generator_func1)) # UNCOMMENT TO RUN : This will generate an exception as end of iterator has been reached : StopIteration