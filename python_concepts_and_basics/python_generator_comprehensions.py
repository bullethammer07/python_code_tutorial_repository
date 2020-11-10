#----------------------------------------
# Python Generator Comprehensions        
#----------------------------------------

# NOTE : Generator Comprehensions use : ()

name_list = ["Jayant", "Nikhil", "Mohit", "Amit", "Parveen"]

# creating a generator using generator comprehension

name_list_genr = (name for name in name_list)

# printing the 'type' of name_list_genr
print(type(name_list_genr)) # This will return : <class 'generator'>

# now we have to iterate over 'name_list_genr' to display the contents
print(next(name_list_genr))
print(next(name_list_genr))
print(next(name_list_genr))
print(next(name_list_genr))
print(next(name_list_genr))