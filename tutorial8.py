str = "Hello World"

print(str[0:7])
print(str[-7:-1])

# ----------------------------------------------------------------------------------------------------------------------
# capitalize()
val = "jayant"
print(val.capitalize()) # To convert the first letter to capitals

#-----------------------------------------------------------------------------------------------------------------------
# casefold() and lower()
val1 = "JAYANT"
print("casefold : ",val1.casefold()) # To convert string to lowercase
print("lower    : ",val1.lower())

# ----------------------------------------------------------------------------------------------------------------------
# center()
val2 = "jayant"
print("center : ",val2.center(50),"end") # Prints the string in the centre of specified number of blank spaces

#-----------------------------------------------------------------------------------------------------------------------
# count()
val3 = "what what what what WHAT WHAT WHAT WHY WHY when when"
print(val3.count("what")) # Counts the number of occurences of a specified value in a string
print(val3.count("WHAT"))
print(val3.count("WHY"))
print(val3.count("when"))

# ----------------------------------------------------------------------------------------------------------------------
# encode()
val4 = "jayant"
print(val4.encode())  #  The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
                      #  Refer :  https://docs.python.org/2.4/lib/standard-encodings.html for a link of all encoding types
"""
------------------------------------------------------------------------------------------------------------------------
endswith()
Syntax : string.endswith(value,start,end)
  value : Required. The value to check of if the string ends with.
  start : Optional. An Integer specifying at which position to start the search
  end   : Optional. An Integer specifying at which position to end the search
"""
val4 = "Hello World"
print(val4.endswith("rld")) # --> Will return as true
print(val4.endswith("Hello World")) # --> Will also return as true. NOTE : Can be used as a method for string match.

"""
------------------------------------------------------------------------------------------------------------------------
expandtabs()
Syntax : string.expandtabs(tabsize)
Description : Replaces any tabs in the string with the specified number of whitespaces
"""
val5 = "Hello\tWorld"
print(val5)
print(val5.expandtabs(100))


# ----------------------------------------------------------------------------------------------------------------------
"""
find()
Syntax : string.find(value)
Description : Returns the index where the match(if found) starts in the string.
               Method returns -1 (type int) is the value is not found.
"""
val6 = "My name is Slim Shady"
print(val6.find("Slim")) # --> Returns Index 11 as 'S' of Slim starts at that location
print(val6.find("xyz"))  # --> This will return -1

#-----------------------------------------------------------------------------------------------------------------------
"""
index()
Syntax : Same as find()
Description : The index() method is almost the same as the find() method, the only difference is that the find() method 
              returns -1 if the value is not found.
"""
ival6 = "My name is Slim Shady"
print("index :",ival6.index("Slim")) # --> Returns Index 11 as 'S' of Slim starts at that location
# print("index :",ival6.index("xyz"))  # --> This will return an exception (Commented out as it will stop the code execution. Uncomment to test)


# ----------------------------------------------------------------------------------------------------------------------
"""
format()
Description : The format() method formats the specified value(s) and insert them inside the string's placeholder.
              The placeholder is defined using curly brackets: {}.
         
Syntax : txt1 = "My name is {fname}, I'am {age}".format(fname = "John", age = 36) --> by name
         txt2 = "My name is {0}, I'am {1}".format("John",36)  --> by index
         txt3 = "My name is {}, I'am {}".format("John",36)  --> by position
"""

val7 = "Hi my name is {name} and I love {hobby}"
print(val7.format(name="Jayant",hobby="Coding"))

# ----------------------------------------------------------------------------------------------------------------------
"""
Below funtions are self explanatory :

isalnum()	    Returns True if all characters in the string are alphanumeric
isalpha()	    Returns True if all characters in the string are in the alphabet
isdecimal()	    Returns True if all characters in the string are decimals
isdigit()	    Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	    Returns True if all characters in the string are lower case
isnumeric()	    Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	    Returns True if all characters in the string are whitespaces
istitle()	    Returns True if the string follows the rules of a title
isupper()	    Returns True if all characters in the string are upper case
"""
#-----------------------------------------------------------------------------------------------------------------------
"""
join()
Description : Joins all items in a tuple into a string  
Syntax : string.join(tuple)
"""
arr = ("This","is","one","sentence")
str1 = "XYX"

x = str1.join(arr)
print("join :",x)
print("join : ","".join(arr))

#-----------------------------------------------------------------------------------------------------------------------
"""
ljust()
Description : appends the character specified number of specified times after the string. Default character is a whitespace
Syntax : string.1just(length,character)  
"""
val8 = "Jayant"
print("ljust : ",val8.ljust(20),"rocks")
print("ljust : ",val8.ljust(15,"x")) # NOTE : The character can only be one character long. Else it will return an exception.

#------------------------------------------------------------------------------------------------------------------------
"""
lstrip() and rstrip()
Description : 
"""