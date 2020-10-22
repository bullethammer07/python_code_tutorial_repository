# --------------------------------------------------------------
#             Python set inbuilt methods
# --------------------------------------------------------------
# add()                    : Method adds a given element to a set. If the element is already present, it doesn't add any element.
# clear()                  : Method removes all elements from the set.
# copy()                   : Method returns a shallow copy of the set.
# difference()             : Method returns the set difference of two sets.
# difference_update()      : Updates the set calling difference_update() method with the difference of sets.
# discard()                : Method removes a specified element from the set (if present).
# intersection()           : Method returns a new set with elements that are common to all sets.
# intersection_update()    : Updates the set calling intersection_update() method with the intersection of sets.
# isdisjoint()             : Method returns True if two sets are disjoint sets. If not, it returns False.
# issubset()               : Method returns True if all elements of a set are present in another set (passed as an argument). If not, it returns False.
# issuperset()             : Method returns True if a set has every elements of another set (passed as an argument). If not, it returns False.
# pop()                    : Method removes an arbitrary element from the set and returns the element removed.
# remove()                 : Method removes the specified element from the set.
# symmetric_difference()   : Method returns the symmetric difference of two sets.
# union()                  : Method returns a new set with distinct elements from all the sets.
# update()                 :

#----------------------------------------------------------------------------------------------------------------------
# add()
# Description : Method adds a given element to a set. If the element is already present, it doesn't add any element.
# Syntax : set.add(elem)
#            elem - the element that is added to the set

print("\n")

# Return Value from Set add()
# add() method doesn't return any value and returns None.

# Example 1: Add an element to a set

# set of vowels
vowels = {'a', 'e', 'i', 'u'}
# adding 'o'
vowels.add('o')
print("add : ", 'Vowels are:', vowels)
# adding 'a' again
vowels.add('a')
print("add : ", 'Vowels are:', vowels)

# Example 2: Add tuple to a set

# set of vowels
vowels2 = {'a', 'e', 'u'}
# a tuple ('i', 'o')
tup = ('i', 'o')
# adding tuple
print("add : ","printing initial set of vowel : ", 'Vowels are:', vowels2)
vowels2.add(tup)
print("add : ","after adding tuple to vowel : ", 'Vowels are:', vowels2)
# adding same tuple again
vowels.add(tup)
print("add : ","after adding the same tuple again to vowel : ",'Vowels are:', vowels2)

#----------------------------------------------------------------------------------------------------------------------
# clear()
# Description : Method removes all elements from the set.
# Syntax : set.clear()
#            clear() method doesn't take any parameters.

print("\n")

# Return value from Set clear()
# clear() method doesn't return any value and returns a None.

# Example 1: Remove all elements from a Python set using clear()

# set of vowels
vowels3 = {'a', 'e', 'i', 'o', 'u'}
print("clear : ", 'Vowels (before clear):', vowels3)
# clearing vowels
vowels3.clear()
print("clear : ", 'Vowels (after clear):', vowels3)

#----------------------------------------------------------------------------------------------------------------------
# copy()
# Description : Method returns a shallow copy of the set.
# Syntax : set.copy()
#            It doesn't take any parameters.

print("\n")

# Return Value from copy()
# The copy() method returns a shallow copy of the set.

# A set can be copied using = operator in Python. For example:
numbers = {1, 2, 3, 4}
new_numbers = numbers

# The problem with copying the set in this way is that if you modify the numbers set, the new_numbers set is also modified. for eg.
new_numbers.add(5)
print("copy : ", "Original Set", 'numbers: ', numbers)
print("copy : ", "Copied Set", 'new_numbers: ', new_numbers)

# However, if you need the original set to be unchanged when the new set is modified, you can use the copy() method.

# Example 1: How the copy() method works for sets?

numbers2 = {1, 2, 3, 4}
new_numbers2 = numbers2.copy()
new_numbers2.add(5)
print("copy : ", "Original Set", 'numbers: ', numbers2)
print("copy : ", "Copied Set", 'new_numbers: ', new_numbers2)

#----------------------------------------------------------------------------------------------------------------------
# difference()
# Description : Method returns the set difference of two sets.
# Syntax : A.difference(B)
#            Here, A and B are two sets. The following syntax is equivalent to A-B.

print("\n")

# Return Value from difference()
# difference() method returns the difference between two sets which is also a set. It doesn't modify original sets.

# Example 1: How difference() works in Python?

A = {'a', 'b', 'c', 'd'}
B = {'c', 'f', 'g'}
# Equivalent to A-B
print("difference : ", A.difference(B))
# Equivalent to B-A
print("difference : ", B.difference(A))

# Example 2: Set Difference Using - Operator.
print("difference : ", A-B)
print("difference : ", B-A)

#----------------------------------------------------------------------------------------------------------------------
# difference_update()
# Description : Updates the set calling difference_update() method with the difference of sets.
# Syntax : A.difference_update(B)
#            Here, A and B are two sets. difference_update() updates set A with the set difference of A-B.

print("\n")

# Return Value from difference_update()
# difference_update() returns None indicating the object (set) is mutated.
# Suppose,
# result = A.difference_update(B)
# When you run the code,
# result will be None
# A will be equal to A-B
# B will be unchanged

# Example: How difference_update() works?

setA = {'a', 'c', 'g', 'd'}
setB = {'c', 'f', 'g'}
result = setA.difference_update(setB)
print("difference_update : ", 'A = ', setA)
print("difference_update : ", 'B = ', setB)
print("difference_update : ", 'result = ', result)

#----------------------------------------------------------------------------------------------------------------------
# discard()
# Description : Method removes a specified element from the set (if present).
# Syntax : s.discard(x)
#            discard() method takes a single element x and removes it from the set (if present).

print("\n")

# Return Value from discard()
# discard() removes element x from the set if the element is present.
# This method returns None (meaning, absence of a return value).

# Example 1: How discard() works?

numbers3 = {2, 3, 4, 5}
numbers3.discard(3)
print("discard : ", 'numbers = ', numbers3)
numbers3.discard(5)
print("discard : ", 'numbers = ', numbers3)
numbers3.discard(10)
print("discard : ", 'numbers = ', numbers3)

#----------------------------------------------------------------------------------------------------------------------
# intersection()
# Description : method returns a new set with elements that are common to all sets.
# Syntax : A.intersection(*other_sets)
#            intersection() allows arbitrary number of arguments (sets).

print("\n")

# Return Value from Intersection()
# intersection() method returns the intersection of set A with all the sets (passed as argument).
# If the argument is not passed to intersection(), it returns a shallow copy of the set (A).

# Example 1: How intersection() works?

set_A = {2, 3, 5, 4}
set_B = {2, 5, 100}
set_C = {2, 3, 8, 9, 10}
print("intersection : ", set_B.intersection(set_A))
print("intersection : ", set_B.intersection(set_C))
print("intersection : ", set_A.intersection(set_C))
print("intersection : ", set_C.intersection(set_A, set_B))

# Example 2 : More Examples

set__A = {100, 7, 8}
set__B = {200, 4, 5}
set__C = {300, 2, 3}
set__D = {100, 200, 300}
print("intersection : ", set__A.intersection(set__D))
print("intersection : ", set__B.intersection(set__D))
print("intersection : ", set__C.intersection(set__D))
print("intersection : ", set__A.intersection(set__B, set__C, set__D))

#----------------------------------------------------------------------------------------------------------------------
# intersection_update()
# Description : Updates the set calling intersection_update() method with the intersection of sets.
# Syntax : A.intersection_update(*other_sets)
#            The intersection_update() method allows an arbitrary number of arguments (sets).

print("\n")

# Return Value from Intersection_update()
# This method returns None (meaning it does not have a return value). It only updates the set calling the intersection_update() method.
# For example:
# result = A.intersection_update(B, C)
# When you run the code,
#   result will be None
#   A will be equal to the intersection of A, B, and C
#   B remains unchanged
#   C remains unchanged

# Example 1: How intersection_update() Works?

set___A = {1, 2, 3, 4}
set___B = {2, 3, 4, 5}
result = set___A.intersection_update(set___B)
print("intersection_update : ", 'result =', result)
print("intersection_update : ", 'A =', set___A)
print("intersection_update : ", 'B =', set___B)

# Example 2: intersection_update() with Two Parameters

SET_A = {1, 2, 3, 4}
SET_B = {2, 3, 4, 5, 6}
SET_C = {4, 5, 6, 9, 10}
result = SET_C.intersection_update(SET_B, SET_A)
print("intersection_update : ", 'result =', result)
print("intersection_update : ", 'C =', SET_C)
print("intersection_update : ", 'B =', SET_B)
print("intersection_update : ", 'A =', SET_A)

#----------------------------------------------------------------------------------------------------------------------
# isdisjoint()
# Description : Method returns True if two sets are disjoint sets. If not, it returns False.
# Syntax : set_a.isdisjoint(set_b)
#            isdisjoint() method takes a single argument (a set).
#            NOTE : You can also pass an iterable (list, tuple, dictionary, and string) to disjoint().
#            isdisjoint() method will automatically convert iterables to set and checks whether the sets are disjoint or not.

print("\n")

# Return Value from isdisjoint()
# isdisjoint() method returns
#   1. True if two sets are disjoint sets (if set_a and set_b are disjoint sets in above syntax)
#   2. False if two sets are not disjoint sets

# Example 1: How isdisjoint() works?

set_a = {1, 2, 3, 4}
set_b = {5, 6, 7}
set_c = {4, 5, 6}
print("isdisjoint : ", 'Are A and B disjoint?', set_a.isdisjoint(set_b))
print("isdisjoint : ", 'Are A and C disjoint?', set_a.isdisjoint(set_c))

# Example 2: isdisjoint() with Other Iterables as arguments

set_aa = {'a', 'b', 'c', 'd'}
set_bb = ['b', 'e', 'f']
set_cc = '5de4'
set_dd = {1 : 'a', 2 : 'b'}
set_ee = {'a' : 1, 'b' : 2}
print("isdisjoint : ", 'Are A and B disjoint?', set_aa.isdisjoint(set_bb))
print("isdisjoint : ", 'Are A and C disjoint?', set_aa.isdisjoint(set_cc))
print("isdisjoint : ", 'Are A and D disjoint?', set_aa.isdisjoint(set_dd))
print("isdisjoint : ", 'Are A and E disjoint?', set_aa.isdisjoint(set_ee))

#----------------------------------------------------------------------------------------------------------------------
# issubset()
# Description : method returns True if all elements of a set are present in another set (passed as an argument). If not, it returns False.
# Syntax : A.issubset(B)
#            The above code checks if A is a subset of B.

print("\n")

# Return Value from issubset()
# issubset() returns
#   True if A is a subset of B
#   False if A is not a subset of B

# Example: How issubset() works?

s_A = {1, 2, 3}
s_B = {1, 2, 3, 4, 5}
s_C = {1, 2, 4, 5}
# Returns True
print("issubset : ", s_A.issubset(s_B))
# Returns False
# B is not subset of A
print("issubset : ", s_B.issubset(s_A))
# Returns False
print("issubset : ", s_A.issubset(s_C))
# Returns True
print("issubset : ", s_C.issubset(s_B))

#----------------------------------------------------------------------------------------------------------------------
# issuperset()
# Description : method returns True if a set has every elements of another set (passed as an argument). If not, it returns False.
# Syntax : A.issuperset(B)
#            The following code checks if A is a superset of B.

print("\n")

# Return Value from issuperset()
# issuperset() returns
#   True if A is a superset of B
#   False if A is not a superset of B

# Example: How issuperset() works?

st_A = {1, 2, 3, 4, 5}
st_B = {1, 2, 3}
st_C = {1, 2, 3}
# Returns True
print("issuperset : ", st_A.issuperset(st_B))
# Returns False
print("issuperset : ", st_B.issuperset(st_A))
# Returns True
print("issuperset : ", st_C.issuperset(st_B))

#----------------------------------------------------------------------------------------------------------------------
# pop()
# Description : Method removes an arbitrary element from the set and returns the element removed.
# Syntax : set.pop()
#            The pop() method doesn't take any arguments.

print("\n")

# Return Value from pop()
# The pop() method returns an arbitrary (random) element from the set. Also, the set is updated and will not contain the element (which is returned).
# If the set is empty, TypeError exception is raised.

# Example: How pop() works for Python Sets?

stA ={'a', 'b', 'c', 'd'}
print("pop : ", 'Return Value is', stA.pop())
print("pop : ", 'A = ', stA)

#----------------------------------------------------------------------------------------------------------------------
# remove()
# Description : Method removes the specified element from the set.
# Syntax : set.remove(element)
#            The remove() method takes a single element as an argument and removes it from the set.

print("\n")

# Return Value from remove()
# The remove() removes the specified element from the set and updates the set. It doesn't return any value.
# If the element passed to remove() doesn't exist, KeyError exception is thrown.

# Example 1: Remove an Element From The Set

# language set
language = {'English', 'French', 'German'}
# removing 'German' from language
print("remove : ", 'Original language set :', language)
language.remove('German')
# Updated language set
print("remove : ", 'Updated language set after remove :', language)

# Example 2: Deleting Element That Doesn't Exist

# animal set
animal = {'cat', 'dog', 'rabbit', 'guinea pig'}
# Deleting 'fish' element
# animal.remove('fish') # UNCOMMENT TO RUN : This will return an exception : KeyError: 'fish'
# Updated animal
# print("remove : ", 'Updated animal set:', animal) # UNCOMMENT TO RUN : This will return an exception : KeyError: 'fish'

#----------------------------------------------------------------------------------------------------------------------
# symmetric_difference()
# Description : Method returns the symmetric difference of two sets.
#               The symmetric difference of two sets A and B is the set of elements that are in either A or B, but not in their intersection.
# Syntax : A.symmetric_difference(B)

print("\n")

# Example 1: Working of symmetric_difference()

p = {'a', 'b', 'c', 'd'}
q = {'c', 'd', 'e' }
r = {}

print("symmetric_difference : ", p.symmetric_difference(q))
print("symmetric_difference : ", q.symmetric_difference(p))
print("symmetric_difference : ", p.symmetric_difference(r))
print("symmetric_difference : ", q.symmetric_difference(r))

# Example : Symmetric difference using ^ operator
# In Python, we can also find the symmetric difference using the ^ operator.

print("symmetric_difference : ", "using ^ operator : ", p ^ q)
print("symmetric_difference : ", "using ^ operator : ", q ^ p)
print("symmetric_difference : ", "using ^ operator : ", p ^ p)
print("symmetric_difference : ", "using ^ operator : ", q ^ q)

#----------------------------------------------------------------------------------------------------------------------
# union()
# Description : Method returns a new set with distinct elements from all the sets.
# Syntax : A.union(*other_sets)
#            NOTE : * is not part of the syntax. It is used to indicate that the method can take 0 or more arguments.

print("\n")

# Return Value from union()
# The union() method returns a new set with elements from the set and all other sets (passed as an argument).
# NOTE : If the argument is not passed to union(), it returns a shallow copy of the set.

# Example 1: Working of union()

us_A = {'a', 'c', 'd'}
us_B = {'c', 'd', 2 }
us_C = {1, 2, 3}
print("union : ", 'A U B =', us_A.union(us_B))
print("union : ", 'B U C =', us_B.union(us_C))
print("union : ", 'A U B U C =', us_A.union(us_B, us_C))
print("union : ", 'A.union() =', us_A.union())

# You can also find the union of sets using the | operator.
# Example 2: Set Union Using the | Operator

print("union : ", "using | operator : ", 'A U B =', us_A | us_B)
print("union : ", "using | operator : ", 'B U C =', us_B | us_C)
print("union : ", "using | operator : ", 'A U B U C =', us_A | us_B | us_C)



#----------------------------------------------------------------------------------------------------------------------
# ()
# Description :
# Syntax :
print("\n")


# ================================================================================================
#                                OUTPUT
# ================================================================================================

