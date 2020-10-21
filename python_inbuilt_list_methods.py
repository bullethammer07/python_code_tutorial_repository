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
# insert()
# Description : Method inserts an element to the list at the specified index.
# Syntax : list.insert(index,element)
#            index : the index where the element needs to be inserted
#            element : this is the element to be inserted in the list
#            NOTE : If index is 0, the element is inserted at the beginning of the list.
#            NOTE : If index is 3, the element is inserted after the 3rd element. Its position will be 4th.

print("\n")

# Return Value from insert()
# The insert() method doesn't return anything; returns None. It only updates the current list.

# Example 1: Inserting an Element to the List

# vowel list
vowel_list4 = ['a', 'e', 'i', 'u']
# 'o' is inserted at index 3
# the position of 'o' will be 4th
vowel_list4.insert(3, 'o')
print("insert : ", 'Updated List:', vowel_list4)

# Example 2: Inserting a Tuple (as an Element) to the List

mixed_list = [{1, 2}, [5, 6, 7]]
# number tuple
number_tuple = (3, 4)
# inserting a tuple to the list
mixed_list.insert(1, number_tuple)
print("insert : ", 'Updated List:', mixed_list)

#----------------------------------------------------------------------------------------------------------------------
# pop()
# Description : Method removes the item at the given index from the list and returns the removed item.
# Syntax : list.pop(index)
#            index : which element at index to pop
#            NOTE : The argument passed to the method is optional. If not passed, the default index -1 is passed as an argument (index of the last item).
#            note : If the index passed to the method is not in range, it throws IndexError: pop index out of range exception.

print("\n")

# Return Value from pop()
# The pop() method returns the item present at the given index. This item is also removed from the list.

# Example 1: Pop item at the given index from the list

# programming languages list
prog_languages = ['Python', 'Java', 'C++', 'French', 'C']
# remove and return the 4th item
return_value = prog_languages.pop(3)
print("pop : ", 'Return Value:', return_value)
# Updated List
print("pop : ", 'Updated List:', prog_languages)


# Example 2: pop() without an index, and for negative indices

# programming languages list
planguages = ['Python', 'Java', 'C++', 'Ruby', 'C']

# remove and return the last item
print("pop : ", 'When index is not passed:')
print("pop : ", 'Return Value:', planguages.pop())
print("pop : ", 'Updated List:', planguages)
# remove and return the last item
print("pop : ", 'When -1 is passed:')
print("pop : ", 'Return Value:', planguages.pop(-1))
print("pop : ", 'Updated List:', planguages)
# remove and return the third last item
print("pop : ", 'When -3 is passed:')
print("pop : ", 'Return Value:', planguages.pop(-3))
print("pop : ", 'Updated List:', planguages)

#----------------------------------------------------------------------------------------------------------------------
# remove()
# Description : Method removes the first matching element (which is passed as an argument) from the list.
# Syntax : list.remove(element)
#            element : the element to remove
#            NOTE : If the element doesn't exist, it throws ValueError: list.remove(x): x not in list exception.

print("\n")

# Return Value from remove()
# The remove() doesn't return any value (returns None).

# Example 1: Remove element from the list

# animals list
animals3 = ['cat', 'dog', 'rabbit', 'guinea pig']
# 'rabbit' is removed
animals3.remove('rabbit')
# Updated animals List
print("remove : ", 'Updated animals list: ', animals3)

# Example 2: remove() method on a list having duplicate elements
# If a list contains duplicate elements, the remove() method only removes the first matching element.

# animals list
animals4 = ['cat', 'dog', 'dog', 'guinea pig', 'dog']
# 'dog' is removed
animals4.remove('dog')
# Updated animals list
print("remove : ", 'Updated animals list: ', animals4)

#----------------------------------------------------------------------------------------------------------------------
# reverse()
# Description : Method reverses the elements of the list.
# Syntax : list.reverse()
#            The reverse() method doesn't take any arguments.

print("\n")

# Return Value from reverse()
# The reverse() method doesn't return any value. It updates the existing list.

# Example 1: Reverse a List

# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print("reverse : ", 'Original List:', systems)
# List Reverse
systems.reverse()
# updated list
print("reverse : ", 'Updated List:', systems)

# Example 2: Reverse a List Using Slicing Operator

# Operating System List
systems2 = ['Windows', 'macOS', 'Linux']
print("reverse list using slicing operator : ", 'Original List:', systems2)
# Reversing a list
#Syntax: reversed_list = systems[start:stop:step]
reversed_list = systems2[::-1]
# updated list
print("reverse list using slicing operator : ", 'Updated List:', reversed_list)

# Example 3: Accessing Elements in Reversed Order
# If you need to access individual elements of a list in the reverse order, it's better to use reversed() function.

# Operating System List
systems3 = ['Windows', 'macOS', 'Linux']
# Printing Elements in Reversed Order
for o in reversed(systems3):
    print("reverse : ", o)

#----------------------------------------------------------------------------------------------------------------------
# sort()
# Description : Method sorts the elements of a given list in a specific ascending or descending order.
# Syntax : list.sort(key=..., reverse=...)
#            NOTE : Alternatively, you can also use Python's built-in sorted() function for the same purpose.
#                   The simplest difference between sort() and sorted() is: sort() changes the list directly and doesn't return any value,
#                   while sorted() doesn't change the list and returns the sorted list.
#            reverse : (Optional), If True, the sorted list is reversed (or sorted in Descending order)
#            key : (Optional), function that serves as a key for the sort comparison

print("\n")

# Return value from sort()
# The sort() method doesn't return any value. Rather, it changes the original list.
# If you want a function to return the sorted list rather than change the original list, use sorted().

# Example 1: Sort a given list

# vowels list
vowels_list4 = ['e', 'a', 'u', 'o', 'i']
# sort the vowels
vowels_list4.sort()
# print vowels
print("sort : ", 'Sorted list:', vowels_list4)

# Sort in Descending order
# The sort() method accepts a reverse parameter as an optional argument.
# Setting reverse = True sorts the list in the descending order.
#   list.sort(reverse=True)
# Alternately for sorted(), you can use the following code.
#   sorted(list, reverse=True)

# Example 2: Sort the list in Descending order

# vowels list
vowels_list5 = ['e', 'a', 'u', 'o', 'i']
# sort the vowels
vowels_list5.sort(reverse=True)
# print vowels
print("sort : ", 'Sorted list (in Descending):', vowels_list5)

# ================================================================================================
#                                OUTPUT
# ================================================================================================

# append :  Updated animals list:  ['cat', 'dog', 'rabbit', 'guinea pig']
# append :  Updated animals list:  ['cat', 'dog', 'rabbit', ['tiger', 'fox']]
#
#
# clear :  printing the list before clearing :  [{1, 2}, 'a', ['1.1', '2.2']]
# clear :  Cleared list: []
# clearing list using del :  printing the list before clearing :  [{1, 2}, 'a', ['1.1', '2.2']]
# clear :  Cleared list: []
#
#
# copying using '=' : [1, 2, 3]
# Printing new_list :  New List: [1, 2, 3, 'a']
# Printing old_list :  Old List: [1, 2, 3, 'a']
# Original List: ['cat', 0, 6.7]
# Copied List: ['cat', 0, 6.7]
# Original List: ['cat', 0, 6.7]
# Copied List: ['cat', 0, 6.7, 'append_val']
# Copying using slicing syntax :  Old List: ['cat', 0, 6.7]
# Copying using slicing syntax :  New List: ['cat', 0, 6.7, 'dog']
#
#
# count :  The count of i is: 2
# count :  The count of p is: 0
# count :  The count of ('a', 'b') is: 2
# count :  The count of [3, 4] is: 1
#
#
# extend :  Language List: ['French', 'English', 'Spanish', 'Portuguese']
# extend :  New Language List: ['French', 'Spanish', 'Portuguese']
# extend :  Newer Language List: ['French', 'Spanish', 'Portuguese', 'Japanese', 'Chinese']
# extend using + operator :  lits a = [1, 2, 3, 4]
# extend using list slicing syntax  lst_a2 = [1, 2, 3, 4]
#
#
# index :  The index of e: 1
# index :  The index of i: 2
# index :  The index of e: 1
# index :  The index of i: 6
#
#
# insert :  Updated List: ['a', 'e', 'i', 'o', 'u']
# insert :  Updated List: [{1, 2}, (3, 4), [5, 6, 7]]
#
#
# pop :  Return Value: French
# pop :  Updated List: ['Python', 'Java', 'C++', 'C']
# pop :  When index is not passed:
# pop :  Return Value: C
# pop :  Updated List: ['Python', 'Java', 'C++', 'Ruby']
# pop :  When -1 is passed:
# pop :  Return Value: Ruby
# pop :  Updated List: ['Python', 'Java', 'C++']
# pop :  When -3 is passed:
# pop :  Return Value: Python
# pop :  Updated List: ['Java', 'C++']
#
#
# remove :  Updated animals list:  ['cat', 'dog', 'guinea pig']
# remove :  Updated animals list:  ['cat', 'dog', 'guinea pig', 'dog']
#
#
# reverse :  Original List: ['Windows', 'macOS', 'Linux']
# reverse :  Updated List: ['Linux', 'macOS', 'Windows']
# reverse list using slicing operator :  Original List: ['Windows', 'macOS', 'Linux']
# reverse list using slicing operator :  Updated List: ['Linux', 'macOS', 'Windows']
# reverse :  Linux
# reverse :  macOS
# reverse :  Windows
#
#
# sort :  Sorted list: ['a', 'e', 'i', 'o', 'u']
# sort :  Sorted list (in Descending): ['u', 'o', 'i', 'e', 'a']