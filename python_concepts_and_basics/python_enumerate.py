# Python enumerate() function

# Usually when using loops (for/while) we need to declare and initialize an external variable and increment inside to keep track of the
# iteration.

# Using enumerate, python returns a numeric index associated with the iterator object passed.
#  refer the examples below :

string = "This is a string with random words"
str_list = string.split()  # converts the above string into a list

print(str_list, type(str_list))

print(list(enumerate(str_list)))  # This will return : [(0, 'This'), (1, 'is'), (2, 'a'), (3, 'string'), (4, 'with'), (5, 'random'), (6, 'words')]
                                  # here each word of the string is associated with its inddex
print(type(enumerate(str_list))) # This will return : <class 'enumerate'>

# NOTE : we can use the enumerate in for loop to get the item along with the index
# this makes iteration simpler. for eg.

for index, val in enumerate(str_list):
    print(f"Index : {index} has string value as : {val}")