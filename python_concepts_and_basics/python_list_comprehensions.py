#-------------------------------
#   Python List Comprehension   
#-------------------------------

# NOTE : List Comprehensions use : []

# List comprehension is an elegant way to define and create lists based on existing lists.

#-----------------------------------------------------------------------------------------------------
# Example 1 : Simple Example
# lets see first how we can iterate through a string using for loop

str_letters = []

for val in 'jayant':
    #print(val)
    str_letters.append(val)
    
print(str_letters)

# However, Python has an easier way to solve this issue using List Comprehension.
# Let’s see how the above program can be written using list comprehensions.

#-----------------------------------------------------------------------------------------------------
# Example 2 : Iterting through a string using List Comprehension

# here we have capitalized each element of the list 'str_letters' and stored it in 'str_letters2'
str_letters2 = [x.upper() for x in str_letters] # example of using List Comprehensions.
print(str_letters2)

# Synatx of List Comprehension
# [expression for item in list]

# replicating Example 1 using List Comprehensions
var1 = [x for x in 'deadpool']
print(var1)

# NOTE : 'deadpool' is a string, not a list. This is the power of list comprehension. 
#        It can identify when it receives a string or a tuple and work on it like a list.

#-----------------------------------------------------------------------------------------------------
# Example 3 : List Comprehensions using Lambda Functions.
#             List comprehensions aren’t the only way to work on lists. Various built-in functions and lambda functions can create and modify lists in less lines of code.

str_letters3 = list(map(lambda x: x, 'Jayant Yadav'))
print(str_letters3)

# NOTE : However, list comprehensions are usually more human readable than lambda functions. 
#        It is easier to understand what the programmer was trying to accomplish when list comprehensions are used.

#-----------------------------------------------------------------------------------------------------
# Example 3 : Conditionals in List Comprehension

#--------------------------------------
# ** Using if with List Comprehension :
num_list = [var for var in range(20) if var % 2 == 0] # makes a list of all even numbers
print(num_list)

#---------------------------------------
# ** Nested If with List Comprehension :
num_list2 = [var for var in range(200) if var % 2 == 0 if var % 5 == 0] # makes a list of all even numbers divisible by 5
print(num_list2)

#--------------------------------------
# ** If-Else with list comprehensions :
obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)

#-----------------------------------------
# ** Nested Loops in List Comprehensions :
# Suppose, we need to compute the transpose of a matrix that requires nested for loop. Let’s see how it is done using normal for loop first.

transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)

# The above code use two for loops to find transpose of the matrix.
# We can also perform nested iteration inside a list comprehension. 
# In this section, we will find transpose of a matrix using nested loop inside list comprehension.

matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print (transpose)