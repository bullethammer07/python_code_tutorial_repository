#-----------------------------------------
# Python Dictionary Comprehensions
#-----------------------------------------

# What is dictionary comprehension ?
# It is an Elegant and concise way to create dictionaries.

#--------------------------------------------------------------------------------------------------------------------------
# Example 1 :

# consider the follwoing code :
square_dict = dict()
for num in range(1, 11):
    square_dict[num] = num*num
print("The created dictionary is : ", square_dict)

# Now lets create the same dictionary above using dictionary comprehensions

square_dict2 = {num: num*num for num in range(1, 11)}
print("Dictionary made using comprehension : ", square_dict2)

#---------------------------------------------------------------------------------------------------------------------------
# The minimal syntax for dictionary comprehension is :

# dictionary = {<key> : <value> for <vars> in <iterable>}
# comparing it with above example we have :

#  {     num       :      num*num       for      num     in     range(1, 11)    }
#         ^                  ^           ^        ^       ^            ^         
#         |                  |           |        |       |            |         
#       <key>      :       <value>      for     <vars>   in        <iterable>    

#--------------------------------------------------------------------------------------------------------------------------
# Example 2 : Using dictionary comprehension using data from another dictionary

# dictionary having price of some items
old_price = {"milk": 25, "coffee": 80, "bread": 40}
print("Old price dict : ", old_price)

# converting old price to new price
added_price = 10
new_price = {item: value + added_price for (item, value) in old_price.items()}
print("New updated price dict : ", new_price)

#------------------------------------------------------
#     Conditionals in Dictionary Comprehensions        
#------------------------------------------------------
# We can further customize dictionary comprehension by adding conditions to it. Let's look at an example.

# If-Conditional Dictionary Comprehension
age_list = {"person1": 15, "person2": 12, "person3": 18, "person4": 20, "person5": 25}
list_adults = {idx: age for (idx, age) in age_list.items() if age > 18} # will make a dictionary containing all people who are 18+
print("list of adults in dictionary is : ", list_adults)

# Multiple If Conditional Dictionary Comprehension
age_list2 = {"person1": 15, "person2": 12, "person3": 18, "person4": 20, "person5": 25, "person6": 29}
list_adult_twenties = {idx: age for (idx, age) in age_list2.items() if age > 18 if age < 30} # will make a dictionary of all adults whose age is less than 30
print("list of adults in dictionary above 18 and below 30 : ", list_adult_twenties)

# If-Else Conditional Comprehension
adult_minor_tag = {idx: ('adult' if age > 18 else 'minor') for (idx, age) in age_list2.items()} # this will make another dictionary with value as 'adult' or 'minor' depending on the age
print("tagged list of adults and minors : ", adult_minor_tag)