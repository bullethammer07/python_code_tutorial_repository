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