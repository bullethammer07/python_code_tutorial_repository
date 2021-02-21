# --------------------------------------------------------------
#             Python tuple inbuilt methods
# --------------------------------------------------------------
# count()    : Method returns the number of times the specified element appears in the tuple.
# index()    : Method returns the index of the specified element in the tuple.

#----------------------------------------------------------------------------------------------------------------------
# count()
# Description : Method returns the number of times the specified element appears in the tuple.
# Syntax : tuple.count(element)
#            element :  the element to be counted

print("\n")

# Return value from count()
# The count() method returns the number of times element appears in the tuple.

# Example 1: Use of Tuple count()

# vowels tuple
vowels = ('a', 'e', 'i', 'o', 'i', 'u')
# count element 'i'
count = vowels.count('i')
# print count
print("count : ", 'The count of i is:', count)
# count element 'p'
count = vowels.count('p')
# print count
print("count : ", 'The count of p is:', count)

# Example 2: Count List and Tuple Elements Inside Tuple

# random tuple
random = ('a', ('a', 'b'), ('a', 'b'), [3, 4])
# count element ('a', 'b')
count = random.count(('a', 'b'))
# print count
print("count : ", "The count of ('a', 'b') is:", count)
# count element [3, 4]
count = random.count([3, 4])
# print count
print("count : ", "The count of [3, 4] is:", count)

#----------------------------------------------------------------------------------------------------------------------
# index()
# Description : Method returns the index of the specified element in the tuple.
# Syntax : tuple.index(element, start, end)
#            element : the element to be searched
#            start : (optional). start searching from this index
#            end : (optional). search the element up to this index

print("\n")

# Return Value from Tuple index()
# The index() method returns the index of the given element in the tuple.
# If the element is not found, a ValueError exception is raised.
# NOTE : The index() method only returns the first occurrence of the matching element.

# Example 1: Find the index of the element

# vowels tuple
vowels2 = ('a', 'e', 'i', 'o', 'i', 'u')
# index of 'e' in vowels
index = vowels2.index('e')
print("index : ", 'The index of e:', index)
# element 'i' is searched
# index of the first 'i' is returned
index = vowels2.index('i')
print("index : ", 'The index of i:', index)

# Example 2: Index of the Element not Present in the Tuple

# vowels tuple
vowels3 = ('a', 'e', 'i', 'o', 'u')
# index of'p' is vowels
# index2 = vowels3.index('p')
# print("index : ", 'The index of p:', index2) # UNCOMMENT TO RUN : This will return an exception

# Example 3: Working of index() With Start and End Parameters

# alphabets tuple
alphabets = ('a', 'e', 'i', 'o', 'g', 'l', 'i', 'u')
# index of 'i' in alphabets
index = alphabets.index('e')   # 2
print("index : ", 'The index of e:', index)
# 'i' after the 4th index is searched
index = alphabets.index('i', 4)   # 6
print("index : ", 'The index of i:', index)
# 'i' between 3rd and 5th index is searched
# index = alphabets.index('i', 3, 5)   # Error!
# print("index : ", 'The index of i:', index) # UNCOMMENT TO RUN : This will return an exception