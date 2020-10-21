#--------------------------------------------------------------
#             Python lists inbuilt methods
#--------------------------------------------------------------
# append()	  *: Adds an element at the end of the list
# clear()	  *: Removes all the elements from the list
# copy()	  *: Returns a copy of the list
# count()	  *: Returns the number of elements with the specified value
# extend()	  *: Add the elements of a list (or any iterable), to the end of the current list
# index()	  *: Returns the index of the first element with the specified value
# insert()	  *: Adds an element at the specified position
# pop()	      *: Removes the element at the specified position
# remove()	  *: Removes the first item with the specified value
# reverse()	  *: Reverses the order of the list
# sort()	  *: Sorts the list

#----------------------------------------------------------------------------------------------------------------------
# append()
# Description : Adds an item to the end of the list.
# Syntax : list.append(item)
#            item : an item to be added at the end of the list

# Return Value from append()
# The method doesn't return any value (returns None).

# Example 1: Adding Element to a List

# animals list
animals = ['cat', 'dog', 'rabbit']
# 'guinea pig' is appended to the animals list
animals.append('guinea pig')
# Updated animals list
print("append : ", 'Updated animals list: ', animals)

# Example 2: Adding List to a List

# animals list
animals2 = ['cat', 'dog', 'rabbit']
# list of wild animals
wild_animals = ['tiger', 'fox']
# appending wild_animals list to the animals list
animals2.append(wild_animals)

print("append : ", 'Updated animals list: ', animals2)

#----------------------------------------------------------------------------------------------------------------------
# clear()
# Description : Method removes all items from the list.
# Syntax : list.clear()

# Return Value from clear()
# The clear() method only empties the given list. It doesn't return any value.

print("\n")

# Example 1: Working of clear() method

# Defining a list
clr_list = [{1, 2}, ('a'), ['1.1', '2.2']]
# printing the list first
print("clear : ", "printing the list before clearing : ", clr_list)
# clearing the list
clr_list.clear()
print("clear : ", 'Cleared list:', clr_list)

# Example 2: Emptying the List Using del

# Defining a list
clr_list2 = [{1, 2}, ('a'), ['1.1', '2.2']]
# printing the list first
print("clearing list using del : ", "printing the list before clearing : ", clr_list2)
# clearing the list
del clr_list2[:]
print("clear : ", 'Cleared list:', clr_list2)

#----------------------------------------------------------------------------------------------------------------------
# copy()
# Description : Method returns a shallow copy of the list.
# Syntax : new_list = list.copy()

print("\n")
# A list can be copied using the = operator. For example,
old_list = [1, 2, 3]
new_list = old_list
print("copying using \'=\' :", new_list)

# NOTE : The problem with copying lists in this way is that if you modify new_list, old_list is also modified.
#        It is because the new list is referencing or pointing to the same old_list object. for eg.

# add an element to list
new_list.append('a')
print("Printing new_list : ", 'New List:', new_list)
print("Printing old_list : ", 'Old List:', old_list)

# However, if you need the original list unchanged when the new list is modified, you can use the copy() method.

# Return Value from copy() :
# The copy() method returns a new list. It doesn't modify the original list.

# Example 1: Copying a List

# mixed list
my_list = ['cat', 0, 6.7]
# copying a list
new_list_cpy = my_list.copy()
print('Original List:', my_list)
print('Copied List:', new_list_cpy)

# modifying new_list_cpy
new_list_cpy.append("append_val")
print('Original List:', my_list)
print('Copied List:', new_list_cpy)

# Example 2: Copy List Using Slicing Syntax
# shallow copy using the slicing syntax

# mixed list
mx_list = ['cat', 0, 6.7]
# copying a list using slicing
new_mx_list = mx_list[:]
# Adding an element to the new list
new_mx_list.append('dog')

# Printing new and old list
print("Copying using slicing syntax : ", 'Old List:', mx_list)
print("Copying using slicing syntax : ", 'New List:', new_mx_list)

#----------------------------------------------------------------------------------------------------------------------
# ()
# Description :
# Syntax :