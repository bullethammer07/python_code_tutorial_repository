#--------------------------------------------------------------
#             Python dictionary inbuilt methods
#--------------------------------------------------------------
# clear()         : Method removes all items from the dictionary.
# copy()          : Method returns a shallow copy of the dictionary.
# fromkeys()     *: Method creates a new dictionary from the given sequence of elements with a value provided by the user.
# get()           : Method returns the value for the specified key if key is in dictionary.
# items()         : Method returns a view object that displays a list of dictionary's (key, value) tuple pairs.
# keys()          : Method returns a view object that displays a list of all the keys in the dictionary
# pop()          *: Method removes and returns an element from a dictionary having the given key.
# popitem()       : Method removes and returns the last element (key, value) pair inserted into the dictionary.
# setdefault()    : Method returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.
# update()        : Updates the dictionary with the elements from the another dictionary object or from an iterable of key/value pairs.
# values()        : Method returns a view object that displays a list of all the values in the dictionary.

#----------------------------------------------------------------------------------------------------------------------
# clear()
# Description : method removes all items from the dictionary.
# Syntax : dict.clear()

print("\n")

# Return Value from clear()
# clear() method doesn't return any value (returns None).

# Example 1: How clear() method works for dictionaries?
dict1 = {1: "one", 2: "two"}
print("clear : ", dict1)
dict1.clear()
print("clear : ", dict1)

#----------------------------------------------------------------------------------------------------------------------
# copy()
# Description : Method returns a shallow copy of the dictionary.
# Syntax : dict.copy()
#            copy() method doesn't take any parameters.

print("\n")

# Return Value from copy()
# This method returns a shallow copy of the dictionary. It doesn't modify the original dictionary.

# Example 1: How copy works for dictionaries?

original_dict = {1:'one', 2:'two'}
new_dict = original_dict.copy()
print("copy : ", 'Orignal: ', original_dict)
print("copy : ", 'New: ', new_dict)

# Difference in Using copy() method, and = Operator to Copy Dictionaries :
#   When copy() method is used, a new dictionary is created which is filled with a copy of the references from the original dictionary.
#   When = operator is used, a new reference to the original dictionary is created.

# Example 2: Using = Operator to Copy Dictionaries

original_dict2 = {1:'one', 2:'two'}
new_dict2 = original_dict2
# removing all elements from the list

# When copied using '=' a new reference to the original dictionary is created.
# therefore any chages in the copy will get reflected in the original as well
# This however isnt the case using copy() method.
new_dict2.clear()
print("copy dict using = operator : ", 'new: ', new_dict2)
print("copy dict using = operator : ", 'original: ', original_dict2)

#----------------------------------------------------------------------------------------------------------------------
# fromkeys()
# Description : Method creates a new dictionary from the given sequence of elements with a value provided by the user.
# Syntax : dictionary.fromkeys(sequence,value)
#            sequence : sequence of elements which is to be used as keys for the new dictionary
#            value : (Optional). value which is set to each each element of the dictionary

print("\n")

# Return value from fromkeys()
# fromkeys() method returns a new dictionary with the given sequence of elements as the keys of the dictionary.
# If the value argument is set, each element of the newly created dictionary is set to the provided value.

# Example 1: Create a dictionary from a sequence of keys

# vowels keys
vowels_keys = {'a', 'e', 'i', 'o', 'u' }
vowels1 = dict.fromkeys(vowels_keys)
print("fromkeys : ", vowels1)

# Example 2: Create a dictionary from a sequence of keys with value

# vowels keys
vowel_keys2 = {'a', 'e', 'i', 'o', 'u' }
value1 = 'vowel'

vowels2 = dict.fromkeys(vowel_keys2, value1)
print("fromkeys : ", vowels2)

# Example 3: Create a dictionary from mutable object list
# If value is a mutable object (whose value can be modified) like list, dictionary, etc., when the mutable object is modified, each element of the sequence also gets updated.
# This is because each element is assigned a reference to the same object (points to the same object in the memory).

# vowels keys
vowel_keys3 = {'a', 'e', 'i', 'o', 'u' }
value2 = [1]
vowels3 = dict.fromkeys(vowel_keys3, value2)
print("fromkeys : ", vowels3)
# updating the value
value2.append(2)
print("fromkeys : ", vowels3)

# To avoid this issue, we use dictionary comprehension.
# Here, for each key in keys, a new list from value is created and assigned to it.
# In essence, value isn't assigned to the element but a new list is created from it, which is then assigned to each element in the dictionary.

# vowels keys
vowel_keys4 = {'a', 'e', 'i', 'o', 'u' }
value3 = [1]

vowels4 = { key : list(value3) for key in vowel_keys4 }
# you can also use { key : value[:] for key in keys }
print("value : ", value3)
print("fromkeys using dictionary comprehension : ", vowels4)
# updating the value
value3.append(2)
# the dictionary vowels will not change even if we have updated the values.
print("value : ", value3)
print("fromkeys using dictionary comprehension : ", vowels4)

#----------------------------------------------------------------------------------------------------------------------
# get()
# Description : Method returns the value for the specified key if key is in dictionary.
# Syntax : dict.get(key[, value])
#            key : key to be searched in the dictionary
#            value : (optional). Value to be returned if the key is not found. The default value is None.

print("\n")

# Return Value from get()
# get() method returns:
#   1. the value for the specified key if key is in dictionary.
#   2. None if the key is not found and value is not specified.
#   3. value if the key is not found and value is specified.

# Example 1: How get() works for dictionaries?

person = {'name': 'Phill', 'age': 22}
print('Name: ', person.get('name'))
print('Age: ', person.get('age'))
# value is not provided
print('Salary: ', person.get('salary')) # This will return None
# value is provided
print('Salary: ', person.get('salary', 0.0)) # This will return 0 as default is provided

# Python get() method Vs dict[key] to Access Elements :
# NOTE : get() method returns a default value if the key is missing.
#        However, if the key is not found when you use dict[key], KeyError exception is raised.

#----------------------------------------------------------------------------------------------------------------------
# items()
# Description : Method returns a view object that displays a list of dictionary's (key, value) tuple pairs.
# Syntax : dictionary.items()
#            items() method is similar to dictionary's viewitems() method in Python 2.7.
#            items() method doesn't take any parameters.

print("\n")

# Return value from items()
# items() method returns a view object that displays a list of a given dictionary's (key, value) tuple pair.

# Example 1: Get all items of a dictionary with items()

# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
print("items : ", sales.items())

# Example 2: How items() works when a dictionary is modified?

# random sales dictionary
sales2 = { 'apple': 2, 'orange': 3, 'grapes': 4 }
sale_items = sales2.items()
print('Original items:', sale_items)
# delete an item from dictionary
del[sales2['apple']]
print('Updated items:', sale_items)

#----------------------------------------------------------------------------------------------------------------------
# keys()
# Description : Method returns a view object that displays a list of all the keys in the dictionary
# Syntax : dict.keys()
#            keys() doesn't take any parameters.

print("\n")

# Return Value from keys()
# keys() returns a view object that displays a list of all the keys.
# When the dictionary is changed, the view object also reflects these changes.

# Example 1: How keys() works?

person1 = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
print("keys : ", person1.keys())
empty_dict = {}
print("keys : ", empty_dict.keys())

# Example 2: How keys() works when dictionary is updated?
# Here, when the dictionary is updated, keys is also automatically updated to reflect changes.

person2 = {'name': 'Phill', 'age': 22, }
print("keys : ", 'Before dictionary is updated', person2.keys())
# adding an element to the dictionary
person2.update({'salary': 3500.0})
print("keys : ", 'After dictionary is updated', person2.keys())

#----------------------------------------------------------------------------------------------------------------------
# pop()
# Description : Method removes and returns an element from a dictionary having the given key.
# Syntax : dictionary.pop(key,default)
#            key : key which is to be searched for removal
#            default : value which is to be returned when the key is not in the dictionary

print("\n")

# Return value from pop()
# The pop() method returns:
#   If key is found - removed/popped element from the dictionary
#   If key is not found - value specified as the second argument (default)
#   If key is not found and default argument is not specified - KeyError exception is raised

# Example 1: Pop an element from the dictionary

# random sales dictionary
sales3 = { 'apple': 2, 'orange': 3, 'grapes': 4 }
element = sales3.pop('apple')
print("pop : ", 'The popped element is:', element)
print("pop : ", 'The dictionary is:', sales3)

# Example 2: Pop an element not present from the dictionary

# random sales dictionary
sales4 = { 'apple': 2, 'orange': 3, 'grapes': 4 }
# element2 = sales4.pop('guava') # UNCOMMENT TO RUN : This will return an exception : KeyError: 'guava'

# Example 3: Pop an element not present from the dictionary, provided a default value

# random sales dictionary
sales5 = { 'apple': 2, 'orange': 3, 'grapes': 4 }
element3 = sales5.pop('guava', 'banana')
print("pop with default : ", 'The popped element is:', element3)
print("pop with default : ", 'The dictionary is:', sales5)

#----------------------------------------------------------------------------------------------------------------------
# popitem()
# Description : Method removes and returns the last element (key, value) pair inserted into the dictionary.
# Syntax : dict.popitem()
#            The popitem() doesn't take any parameters.

print("\n")

# Return Value from popitem() method
# The popitem() method removes and returns the (key, value) pair from the dictionary in the Last In, First Out (LIFO) order.
#   1. Returns the latest inserted element (key,value) pair from the dictionary.
#   2. Removes the returned element pair from the dictionary.

# Example 1 : Working of popitem() method

person3 = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
# ('salary', 3500.0) is inserted at the last, so it is removed.
print("popitem : ", 'Initial Value = ', person3)
result = person3.popitem()
print("popitem : ", 'popitem Value = ', result)
print("popitem : ", 'updated person dict = ', person3)
# inserting a new element pair
person3['profession'] = 'Plumber'
print("popitem : ", 'Added item to person dict = ', result)
print("popitem : ", 'updated person dict = ', person3)
# popping last item
result = person3.popitem()
print("popitem : ", 'person updated dict after popitem ', person3)

#----------------------------------------------------------------------------------------------------------------------
# setdefault()
# Description : Method returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.
# Syntax : dict.setdefault(key,default_value)
#            key : the key to be searched in the dictionary
#            default_value : (optional). key with a value default_value is inserted to the dictionary if the key is not in the dictionary.
#                            If not provided, the default_value will be None.

print("\n")

# Return Value from setdefault() :
# setdefault() returns:
#   1. value of the key if it is in the dictionary
#   2. None if the key is not in the dictionary and default_value is not specified
#   3. default_value if key is not in the dictionary and default_value is specified

# Example 1: How setdefault() works when key is in the dictionary?

person4 = {'name': 'Phill', 'age': 22}
person4_age = person4.setdefault('age')
print("setdefault : ", 'person = ',person4)
print("setdefault : ", 'Age = ', person4_age)

# Example 2: How setdefault() works when key is not in the dictionary?

person5 = {'name': 'Phill'}
# key is not in the dictionary
person5_salary = person5.setdefault('salary')
print("setdefault : ", 'person = ', person5)
print("setdefault : ", 'salary = ', person5_salary)
# key is not in the dictionary
# default_value is provided
person5_age = person5.setdefault('age', 22)
print("setdefault : ", 'person = ', person5)
print("setdefault : ", 'age = ', person5_age)

#----------------------------------------------------------------------------------------------------------------------
# update()
# Description : Updates the dictionary with the elements from the another dictionary object or from an iterable of key/value pairs.
# Syntax : dict.update([other])
#            The update() method takes either a dictionary or an iterable object of key/value pairs (generally tuples).
#            NOTE : If update() is called without passing parameters, the dictionary remains unchanged.

print("\n")

# Return Value from update()
# update() method updates the dictionary with elements from a dictionary object or an iterable object of key/value pairs.
#   It doesn't return any value (returns None).

# Example 1: Working of update()

d = {1: "one", 2: "three"}
d1 = {2: "two"}
# updates the value of key 2
d.update(d1)
print("update : ", d)
d1 = {3: "three"}
# adds element with key 3
d.update(d1)
print("update : ", d)

# Example 2: update() When Tuple is Passed
d2 = {'x': 2}
d2.update(y = 3, z = 0)
print("update : ", d2)

#----------------------------------------------------------------------------------------------------------------------
# values()
# Description : Method returns a view object that displays a list of all the values in the dictionary.
# Syntax : dictionary.values()
#            values() method doesn't take any parameters.

print("\n")

# Return value from values()
# values() method returns a view object that displays a list of all values in a given dictionary.

# Example 1: Get all values from the dictionary

# random sales dictionary
sales6 = { 'apple': 2, 'orange': 3, 'grapes': 4 }
print("values : ", sales6.values())

# Example 2: How values() works when dictionary is modified?

# random sales dictionary
sales7 = { 'apple': 2, 'orange': 3, 'grapes': 4 }
sales7_values = sales7.values()
print("values : ", 'Original items:', sales7_values)
# delete an item from dictionary
del[sales7['apple']]
print("values : ", 'Updated items:', sales7_values)

# ================================================================================================
#                                OUTPUT
# ================================================================================================

# clear :  {1: 'one', 2: 'two'}
# clear :  {}
#
#
# copy :  Orignal:  {1: 'one', 2: 'two'}
# copy :  New:  {1: 'one', 2: 'two'}
# copy dict using = operator :  new:  {}
# copy dict using = operator :  original:  {}
#
#
# fromkeys :  {'e': None, 'u': None, 'a': None, 'i': None, 'o': None}
# fromkeys :  {'e': 'vowel', 'u': 'vowel', 'a': 'vowel', 'i': 'vowel', 'o': 'vowel'}
# fromkeys :  {'e': [1], 'u': [1], 'a': [1], 'i': [1], 'o': [1]}
# fromkeys :  {'e': [1, 2], 'u': [1, 2], 'a': [1, 2], 'i': [1, 2], 'o': [1, 2]}
# value :  [1]
# fromkeys using dictionary comprehension :  {'e': [1], 'u': [1], 'a': [1], 'i': [1], 'o': [1]}
# value :  [1, 2]
# fromkeys using dictionary comprehension :  {'e': [1], 'u': [1], 'a': [1], 'i': [1], 'o': [1]}
#
#
# Name:  Phill
# Age:  22
# Salary:  None
# Salary:  0.0
#
#
# items :  dict_items([('apple', 2), ('orange', 3), ('grapes', 4)])
# Original items: dict_items([('apple', 2), ('orange', 3), ('grapes', 4)])
# Updated items: dict_items([('orange', 3), ('grapes', 4)])
#
#
# keys :  dict_keys(['name', 'age', 'salary'])
# keys :  dict_keys([])
# keys :  Before dictionary is updated dict_keys(['name', 'age'])
# keys :  After dictionary is updated dict_keys(['name', 'age', 'salary'])
#
#
# pop :  The popped element is: 2
# pop :  The dictionary is: {'orange': 3, 'grapes': 4}
# pop with default :  The popped element is: banana
# pop with default :  The dictionary is: {'apple': 2, 'orange': 3, 'grapes': 4}
#
#
# popitem :  Initial Value =  {'name': 'Phill', 'age': 22, 'salary': 3500.0}
# popitem :  popitem Value =  ('salary', 3500.0)
# popitem :  updated person dict =  {'name': 'Phill', 'age': 22}
# popitem :  Added item to person dict =  ('salary', 3500.0)
# popitem :  updated person dict =  {'name': 'Phill', 'age': 22, 'profession': 'Plumber'}
# popitem :  person updated dict after popitem  {'name': 'Phill', 'age': 22}
#
#
# setdefault :  person =  {'name': 'Phill', 'age': 22}
# setdefault :  Age =  22
# setdefault :  person =  {'name': 'Phill', 'salary': None}
# setdefault :  salary =  None
# setdefault :  person =  {'name': 'Phill', 'salary': None, 'age': 22}
# setdefault :  age =  22
#
#
# update :  {1: 'one', 2: 'two'}
# update :  {1: 'one', 2: 'two', 3: 'three'}
# update :  {'x': 2, 'y': 3, 'z': 0}
#
#
# values :  dict_values([2, 3, 4])
# values :  Original items: dict_values([2, 3, 4])
# values :  Updated items: dict_values([3, 4])