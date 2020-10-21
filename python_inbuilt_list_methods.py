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
# pop()       *: Removes the element at the specified position
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
# count()
# Description : Method returns the number of times the specified element appears in the list.
# Syntax : list.count(element)
#            element : the element to be counted

print("\n")

# Return value from count()
# The count() method returns the number of times element appears in the list.

# Example 1: Use of count()

# vowels list
vowels_list = ['a', 'e', 'i', 'o', 'i', 'u']
# count element 'i'
count1 = vowels_list.count('i')
# print count
print("count : ", 'The count of i is:', count1)
# count element 'p'
count1 = vowels_list.count('p')
# print count
print("count : ", 'The count of p is:', count1)

# Example 2: Count Tuple and List Elements Inside List

# random list
random_list = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]
# count element ('a', 'b')
count2 = random_list.count(('a', 'b'))
# print count
print("count : ", "The count of ('a', 'b') is:", count2)
# count element [3, 4]
count2 = random_list.count([3, 4])
# print count
print("count : ", "The count of [3, 4] is:", count2)

#----------------------------------------------------------------------------------------------------------------------
# extend()
# Description : Method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.
# Syntax : list1.extend(iterable)
#             Here, all the elements of iterable are added to the end of list1.

print("\n")

# Return Value from extend()
# The extend() method modifies the original list. It doesn't return any value.

# Example 1: Using extend() Method

# language list
language = ['French', 'English']
# another list of language
language1 = ['Spanish', 'Portuguese']
# appending language1 elements to language
language.extend(language1)
print("extend : ", 'Language List:', language)

# Example 2: Add Elements of Tuple and Set to List

# language list
language_list = ['French']
# language tuple
language_tuple = ('Spanish', 'Portuguese')
# language set
language_set = {'Chinese', 'Japanese'}
# appending language_tuple elements to language_list
language_list.extend(language_tuple)
print("extend : ", 'New Language List:', language_list)
# appending language_set elements to language_list
language_list.extend(language_set)
print("extend : ", 'Newer Language List:', language_list)

# Other ways to extend a list :

# Example 3 : the + operator

lsta = [1, 2]
lstb = [3, 4]
lsta += lstb    # a = a + b
# Output: [1, 2, 3, 4]
print("extend using + operator : ", 'lits a =', lsta)

# Example 4 : the list slicing syntax

lst_a2 = [1, 2]
lst_b2 = [3, 4]
lst_a2[len(lst_a2):] = lst_b2
# Output: [1, 2, 3, 4]
print("extend using list slicing syntax ", 'lst_a2 =', lst_a2)

#----------------------------------------------------------------------------------------------------------------------
# index()
# Description : Method returns the index of the specified element in the list.
# Syntax : list.index(element, start, end)
#            element : the element to be searched
#            start : (optional). start searching from this index
#            end : (optional). search the element up to this index

# Return Value from List index()
# The index() method returns the index of the given element in the list.
# If the element is not found, a ValueError exception is raised.
# NOTE : The index() method only returns the first occurrence of the matching element.

print("\n")

# Example 1 : Find the index of the element

# vowels list
vowels_list2 = ['a', 'e', 'i', 'o', 'i', 'u']
# index of 'e' in vowels
idx = vowels_list2.index('e')
print("index : ", 'The index of e:', idx)
# element 'i' is searched
# index of the first 'i' is returned
idx = vowels_list2.index('i')
print("index : ", 'The index of i:', idx)

# Example 2: Index of the Element not Present in the List

# vowels list
vowels_list3 = ['a', 'e', 'i', 'o', 'u']
# index of 'p' is vowels
# idx = vowels_list3.index('p') # UNCOMMENT TO RUN
# print("index : ", 'The index of p:', idx) # UNCOMMENT TO RUN : This will return an exeception : ValueError: 'p' is not in list

# Example 3: Working of index() With Start and End Parameters

# alphabets list
alphabets_list = ['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u']
# index of 'i' in alphabets
idx = alphabets_list.index('e')   # 2
print("index : ", 'The index of e:', idx)
# 'i' after the 4th index is searched
idx = alphabets_list.index('i', 4)   # 6
print("index : ", 'The index of i:', idx)
# 'i' between 3rd and 5th index is searched
# idx = alphabets_list.index('i', 3, 5)   # Error! # UNCOMMENT TO RUN :
# print("index : ", 'The index of i:', idx) # UNCOMMENT TO RUN : This will return an exception as the item will not be found.




#----------------------------------------------------------------------------------------------------------------------
# ()
# Description :
# Syntax :