# Conditionals in Python
#   1. if
#        'in' keyowrd
#        'not in' keyword
#   2. if else
#   3. if elif
#   4. for loop
#   5. for loop with else
#   6. while loop
#   7. while loop with else
#   8. break and continue
#   9. Pass statement

# Python supports the usual logical conditions from mathematics:
#   Equals: a == b
#   Not Equals: a != b
#   Less than: a < b
#   Less than or equal to: a <= b
#   Greater than: a > b
#   Greater than or equal to: a >= b

#-------------------------------------------------------------------------------------------------------------------
# If Statement :
# if test expression:
#     statement(s)

# Here, the program evaluates the test expression and will execute statement(s) only if the test expression is True.
# NOTE : Python interprets non-zero values as True. None and 0 are interpreted as False.

# If the number is positive, we print an appropriate message

num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")

#-------------------------------------------------------------------------------------------------------------------
# If else statement :

# Take input from user
choice = input("Do you want to continus ? (Y/N): ")

if choice == 'Y':
    print("Yes the user wants to continue")
else:
    print("The user does not want to continue")

#-------------------------------------------------------------------------------------------------------------------
# If else-If statement :

choice2 = input("Do you want to enter the store ? (Y/N) : ")

if choice2 == 'Y':
    print("Welcome to the store")
elif choice2 == 'N':
    print("Please visit soon :) !!...")

# 'in' and 'not in' keyowrd in if statements
# can be clubbed  with if statements to checky if an element is present in an iterable. for eg

# NOTE :
# the statements '<var> in <iterable>' and '<var> not in <iterable>' can return True or False based on the conditions.
# These can be used indifferent area where True/False judgement is required

str1 = "This is a string"
list2 = str1.split()

if 'This' in list2: # Checks for keyword 'This' in the list list2
    print("Element found")

#-------------------------------------------------------------------------------------------------------------------
# for loop
# The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects. Iterating over a sequence is called traversal.

# syntax : for val in sequence:
# 	           body of for

# Here, val is the variable that takes the value of the item inside the sequence on each iteration.
# Loop continues until we reach the last item in the sequence. The body of for loop is separated from the rest of the code using indentation.

# Example

numbers = [1, 2, 3, 4, 5, 6, 7]

for var in numbers:
    print("Current value is :: ", var)

