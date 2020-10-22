# --------------------------------------------------------------
#             Python set inbuilt methods
# --------------------------------------------------------------
# add()                    : Method adds a given element to a set. If the element is already present, it doesn't add any element.
# clear()                  : Method removes all elements from the set.
# copy()                   : Method returns a shallow copy of the set.
# difference()             :
# difference_update()      :
# discard()                :
# intersection()           :
# intersection_update()    :
# isdisjoint()             :
# issubset()               :
# issuperset()             :
# pop()                    :
# remove()                 :
# symmetric_difference()   :
# union()                  :
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
# ()
# Description :
# Syntax :
print("\n")




# ================================================================================================
#                                OUTPUT
# ================================================================================================

