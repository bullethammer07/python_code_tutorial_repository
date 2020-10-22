#--------------------------------------------------------------
#             Python dictionary inbuilt methods
#--------------------------------------------------------------
# clear()         : Method removes all items from the dictionary.
# copy()          : Method returns a shallow copy of the dictionary.
# fromkeys()     *: Method creates a new dictionary from the given sequence of elements with a value provided by the user.
# get()           :
# items()         :
# keys()          :
# pop()           :
# popitem()       :
# setdefault()    :
# update()        :
# values()        :

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
# ()
# Description :
# Syntax :
print("\n")