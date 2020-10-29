#-----------------
# Python Iterator
#-----------------

# Iterators are objects that can be iterated upon
# Technically speaking, a Python iterator object must implement two special methods, __iter__() and __next__(), collectively called the iterator protocol.
# An object is called iterable if we can get an iterator from it. Most built-in containers in Python like: list, tuple, string etc. are iterables.
# NOTE : The iter() function (which in turn calls the __iter__() method) returns an iterator from them.

#-----------------------------------------------------------------------------------------------------------
# Example 1 : Iterating Through an Iterator
# We use the next() function to manually iterate through all the items of an iterator.
# When we reach the end and there is no more data to be returned, it will raise the StopIteration Exception. Following is an example.

print("\n")

list1 = [1, 2, 3, 4]

# get an iterator using iter()
list1_iter = iter(list1)

# Iterate through the iterator using next()
print(next(list1_iter))  # prints 1
print(next(list1_iter))  # prints 2

# next(obj) is same as obj.__next__()
print(list1_iter.__next__())  # prints 3
print(list1_iter.__next__())  # prints 4

try:
    print(next(list1_iter)) # This will generate an exception as no further items are there in the iterator.
except Exception as e:
    print("Exception generated : ")

#-----------------------------------------------------------------------------------------------------------
# Example 2 : Iterating using for loop.
#             The usual for loop  is more better method for iterating over the list or iterable object.

print("\n")
for item in list1:
    print(f"The item is {item}")

#-----------------------------------------------------------------------------------------------------------
# Example 3 : Working of for loop for Iterators
#             As we see in the above example, the for loop was able to iterate automatically through the list.
#             NOTE : In fact the for loop can iterate over any iterable. Let's take a closer look at how the for loop is actually implemented in Python.

print("\n")

# for element in iterable:
#     # do something with element

# Is actually implemented a :

list2 = [1, 2, 3, 4, 5, 6, 7]
list2_iter = iter(list2)

while True:
    try:
        # get the next element
        element = next(list2_iter)
        print(f"for implemented using while : {element}")
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break

#-----------------------------------------------------------------------------------------------------------
# Example 3 : Building Custom Iterators
#             Building an iterator from scratch is easy in Python. We just have to implement the __iter__() and the __next__() methods.
#               1. The __iter__() method returns the iterator object itself. If required, some initialization can be performed.
#               2. The __next__() method must return the next item in the sequence. On reaching the end, and in subsequent calls, it must raise StopIteration.

# Here, we show an example that will give us the next power of 2 in each iteration. Power exponent starts from zero up to a user set number.

print("\n")

class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

# create an object
numbers = PowTwo(3)

# create an iterable from the object
i = iter(numbers)

# Using next to get to the next iterator element
print("Custom iterator : ", next(i))
print("Custom iterator : ", next(i))
print("Custom iterator : ", next(i))
print("Custom iterator : ", next(i))
# print("Custom iterator : ", next(i)) # UNCOMMENT TO RUN : This will generate an exception as end of iterator object has been reached.