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
