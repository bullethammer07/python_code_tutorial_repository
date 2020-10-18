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

# ------------------------------------------------------------------------------------------------------------------------
# endswith()
# Syntax : string.endswith(value,start,end)
#   value : Required. The value to check of if the string ends with.
#   start : Optional. An Integer specifying at which position to start the search
#   end   : Optional. An Integer specifying at which position to end the search

val4 = "Hello World"
print(val4.endswith("rld")) # --> Will return as true
print(val4.endswith("Hello World")) # --> Will also return as true. NOTE : Can be used as a method for string match.

# ------------------------------------------------------------------------------------------------------------------------
# expandtabs()
# Syntax : string.expandtabs(tabsize)
# Description : Replaces any tabs in the string with the specified number of whitespaces

val5 = "Hello\tWorld"
print(val5)
print(val5.expandtabs(100))


# ----------------------------------------------------------------------------------------------------------------------
# find()
# Syntax : string.find(value)
# Description : Returns the index where the match(if found) starts in the string.
#                Method returns -1 (type int) is the value is not found.

val6 = "My name is Slim Shady"
print(val6.find("Slim")) # --> Returns Index 11 as 'S' of Slim starts at that location
print(val6.find("xyz"))  # --> This will return -1

#-----------------------------------------------------------------------------------------------------------------------
# index()
# Syntax : Same as find()
# Description : The index() method is almost the same as the find() method, the only difference is that the find() method
#               returns -1 if the value is not found.

ival6 = "My name is Slim Shady"
print("index :",ival6.index("Slim")) # --> Returns Index 11 as 'S' of Slim starts at that location
# print("index :",ival6.index("xyz"))  # --> This will return an exception (Commented out as it will stop the code execution. Uncomment to test)


# ----------------------------------------------------------------------------------------------------------------------
# format()
# Description : The format() method formats the specified value(s) and insert them inside the string's placeholder.
#               The placeholder is defined using curly brackets: {}.
#
# Syntax : txt1 = "My name is {fname}, I'am {age}".format(fname = "John", age = 36) --> by name
#          txt2 = "My name is {0}, I'am {1}".format("John",36)  --> by index
#          txt3 = "My name is {}, I'am {}".format("John",36)  --> by position

val7 = "Hi my name is {name} and I love {hobby}"
print(val7.format(name="Jayant",hobby="Coding"))

# ----------------------------------------------------------------------------------------------------------------------

# Below funtions are self explanatory :
#
# isalnum()	    Returns True if all characters in the string are alphanumeric
# isalpha()	    Returns True if all characters in the string are in the alphabet
# isdecimal()	    Returns True if all characters in the string are decimals
# isdigit()	    Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	    Returns True if all characters in the string are lower case
# isnumeric()	    Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	    Returns True if all characters in the string are whitespaces
# istitle()	    Returns True if the string follows the rules of a title
# isupper()	    Returns True if all characters in the string are upper case

#-----------------------------------------------------------------------------------------------------------------------

# join()
# Description : Joins all items in a tuple into a string
# Syntax : string.join(tuple)

arr = ("This","is","one","sentence")
str1 = "XYX"

x = str1.join(arr)
print("join :",x)
print("join : ","".join(arr))

#-----------------------------------------------------------------------------------------------------------------------
# ljust()
# Description : appends the character specified number of specified times after the string. Default character is a whitespace
# Syntax : string.1just(length,character)

val8 = "Jayant"
print("ljust : ",val8.ljust(20),"rocks")
print("ljust : ",val8.ljust(15,"x")) # NOTE : The character can only be one character long. Else it will return an exception.

#------------------------------------------------------------------------------------------------------------------------
# lstrip() and rstrip()
# Description : lstrip() removes any whitespaces at the left of the string
#               rstrip() removes any whitespaces at the right of the string
#
# Syntax : string.lstrip(characters)   --> You can specify a set of characters to removes from the start
#          string.rstrip(characters)

val9 = "          My name is Slim Shady          "
val10 = ".....,,,,,$$$$$#####^^^^^Banana&&&***)))@@@"

print("lstrip : ",val9.lstrip(),"end")
print("rstrip : ",val9.rstrip(),"end")
print("lstrip : ",val10.lstrip(".,$#^"),"end")
print("lstrip : ",val10.rstrip("&*)@"),"end")

#-----------------------------------------------------------------------------------------------------------------------------
# translate() and maketrans()
# Description : the translate() method returns a string where some specified characters are replaced with the characters described in
#               a dictionary, or in a mapping table.
#               -> Use the maketrans() method to create a mapping table
# Syntax : string.translate(table)    <- table can be created with maketrans()
#          table : Required. Either a 'dictionary' , or a 'mapping table' describing how to perform the replace

txt = "Hello Sam!"
my_table = txt.maketrans("Sa","Ta") # NOTE : The replacement character must be of the same length as the character(s) that need to be replaced.
                                    # for eg . valid combinations are : ("S","T") , ("Sa","Ta") , ("Sam","Tam")
print("translate : ",type(my_table),txt.translate(my_table)) # Output of type is L <class 'dict'>

# OUT OF ORDER ARGUMENTS :
# There is a respective one to one mapping in the arguments of maketrans() of the characters to specify to replace, for eg :
# If you specify ("mSa","eJo") , then 'm' corresponds to be replaced with 'e'
#                                     'S' corresponds to be replaced with 'J'
#                                     'a' corresponds to be replaced with 'o'
# Hence, even if the characters to be replaced are out of order as specified. In the output 'Sam' will still be replaced with 'Joe'
# refer example below
my_table2 = txt.maketrans("mSa","eJo")
print("translate : ",txt.translate(my_table2))

# CHARACTERS TO BE REMOVED FROM THE STRING
# You can also specify a third character in the maketrans() that will create a mapping table with the specified character removed. for eg :

txt2 = "This is a simple text message"
my_table3 = txt.maketrans("simple","simple","message") # individual characters of 'message' will be removed from the complete text
print("translate : ",txt2.translate(my_table3))

#---------------------------------------------------------------------------------------------------------------------------------
# partition()
# Description : the method searches for a specified string, and splits the string into a tuple containing three elements
#               The first element contains the part before the string
#               The second element contains the specified string
#               The third element contains the part after the string

txt3 = "This is before the string match match_value This is after the string match"
print("partition  : ",txt3.partition("match_value"))

#---------------------------------------------------------------------------------------------------------------------------------
# replace()
# Description : Replaces a specified phrase with another specified phrase
# Syntax : string.replace(oldvalue , newvalue , count)
#          oldvalue : the phrase to be replaced
#          newvalue : new value with with the older phrase has to be replaced with
#          count    :  (Optionl) . A number specifying how many occurrences of the old value you want to replace. Default is all occurrences

txt4 = "The quick brown fox fox fox fox fox fox fox jumps over the lazy dog"

print("replace : ",txt4.replace("fox","tiger"))  # This will replace all occurrences of 'fox' with 'tiger'
print("replace : ",txt4.replace("fox","wolf",4)) # This will replace the first 4 occurences of 'fox' with 'wolf'