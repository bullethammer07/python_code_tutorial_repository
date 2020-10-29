str = "Hello World"

print("using +ve and -ve indexes : ",str[0:7])
print("using +ve and -ve indexes : ",str[-7:-1])

#-----------------------------------------------------------------------------------
#                        Python Inbuilt String Methods
#-----------------------------------------------------------------------------------
# capitalize()	    : Converts the first character to upper case
# casefold()	    : Converts string into lower case
# center()	        : Returns a centered string
# count()	        : Returns the number of times a specified value occurs in a string
# encode()	        : Returns an encoded version of the string
# endswith()	    : Returns true if the string ends with the specified value
# expandtabs()	    : Sets the tab size of the string
# find()	        : Searches the string for a specified value and returns the position of where it was found
# format()	        : Formats specified values in a string
# format_map()	    : Formats specified values in a string
# index()	        : Searches the string for a specified value and returns the position of where it was found
# isalnum()	        : Returns True if all characters in the string are alphanumeric
# isalpha()	        : Returns True if all characters in the string are in the alphabet
# isdecimal()	    : Returns True if all characters in the string are decimals
# isdigit()	        : Returns True if all characters in the string are digits
# isidentifier()	: Returns True if the string is an identifier
# islower()	        : Returns True if all characters in the string are lower case
# isnumeric()	    : Returns True if all characters in the string are numeric
# isprintable()	    : Returns True if all characters in the string are printable
# isspace()	        : Returns True if all characters in the string are whitespaces
# istitle()	        : Returns True if the string follows the rules of a title
# isupper()	        : Returns True if all characters in the string are upper case
# join()	        : Joins the elements of an iterable to the end of the string
# ljust()	        : Returns a left justified version of the string
# lower()	        : Converts a string into lower case
# lstrip()	        : Returns a left trim version of the string
# maketrans()	    : Returns a translation table to be used in translations
# partition()	    : Returns a tuple where the string is parted into three parts
# replace()	        : Returns a string where a specified value is replaced with a specified value
# rfind()	        : Searches the string for a specified value and returns the last position of where it was found
# rindex()	        : Searches the string for a specified value and returns the last position of where it was found
# rjust()	        : Returns a right justified version of the string
# rpartition()	    : Returns a tuple where the string is parted into three parts
# rsplit()	        : Splits the string at the specified separator, and returns a list
# rstrip()	        : Returns a right trim version of the string
# split()	        : Splits the string at the specified separator, and returns a list
# splitlines()	    : Splits the string at line breaks and returns a list
# startswith()	    : Returns true if the string starts with the specified value
# strip()	        : Returns a trimmed version of the string
# swapcase()	    : Swaps cases, lower case becomes upper case and vice versa
# title()	        : Converts the first character of each word to upper case
# translate()	    : Returns a translated string
# upper()	        : Converts a string into upper case
# zfill()	        : Fills the string with a specified number of 0 values at the beginning

# ----------------------------------------------------------------------------------------------------------------------
# capitalize()
val = "jayant yadav"
print("capitalize : ",val.capitalize()) # To convert the first letter to capitals

#-----------------------------------------------------------------------------------------------------------------------
# upper()
# Description : Converts all characters in a string to uppercase
# Syntax : string.upper()

valx = "all characters are lowercase"
print("upper : ",valx.upper())

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
print("count : ",val3.count("what")) # Counts the number of occurences of a specified value in a string
print("count : ",val3.count("WHAT"))
print("count : ",val3.count("WHY"))
print("count : ",val3.count("when"))

# ----------------------------------------------------------------------------------------------------------------------
# encode()
val4 = "jayant"
print("encode : ",val4.encode())  #  The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
                      #  Refer :  https://docs.python.org/2.4/lib/standard-encodings.html for a link of all encoding types

# ------------------------------------------------------------------------------------------------------------------------
# endswith() and startswith()
# Description : The startswith() method returns True if the string starts with the specified value, otherwise False.
#               The endswith() method returns True if the string ends with the specified value, otherwise False.
# Syntax : string.endswith(value,start,end)
#          string.startswith(value,start,end)
#          value : Required. The value to check of if the string ends with.
#          start : Optional. An Integer specifying at which position to start the search
#          end   : Optional. An Integer specifying at which position to end the search

val4 = "Hello World"
print("endswith : ",val4.endswith("rld")) # --> Will return as true
print("endswith : ",val4.endswith("Hello World")) # --> Will also return as true. NOTE : Can be used as a method for string match.
print("startswith : ",val4.startswith("Hel")) # --> Will return as true
print("startswith : ",val4.startswith("Hello World")) # --> Will also return as true. NOTE : Can be used as a method for string match.

# ------------------------------------------------------------------------------------------------------------------------
# expandtabs()
# Syntax : string.expandtabs(tabsize)
# Description : Replaces any tabs in the string with the specified number of whitespaces

val5 = "Hello\tWorld"
print("expandtabs : ",val5)
print("expandtabs : ",val5.expandtabs(100))


# ----------------------------------------------------------------------------------------------------------------------
# find()
# Syntax : string.find(value)
# Description : Returns the index where the match(if found) starts in the string.
#                Method returns -1 (type int) is the value is not found.

val6 = "My name is Slim Shady"
print("find : ",val6.find("Slim")) # --> Returns Index 11 as 'S' of Slim starts at that location
print("find : ",val6.find("xyz"))  # --> This will return -1

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
print("format : ",val7.format(name="Jayant",hobby="Coding"))

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
# ljust() and rjust()
# Description : ljust() appends the character specified number of specified times after the string. Default character is a whitespace
#               rjust() appends the character specified number of specified times before the string. Default character is a whitespace
# Syntax : string.1just(length,character)

val8 = "Jayant"
print("ljust : ",val8.ljust(20),"rocks")
print("ljust : ",val8.ljust(15,"x")) # NOTE : The character can only be one character long. Else it will return an exception.
print("rjust : ",val8.rjust(20),"rocks")
print("rjust : ",val8.rjust(15,"x"))

#------------------------------------------------------------------------------------------------------------------------
# lstrip() and rstrip() and strip()
# Description : lstrip() removes any whitespaces at the left of the string
#               rstrip() removes any whitespaces at the right of the string
#               strip() removes any whitespaces at both ends of the string
#
# Syntax : string.lstrip(characters)   --> You can specify a set of characters to removes from the start
#          string.rstrip(characters)

val9 = "          My name is Slim Shady          "
val10 = ".....,,,,,$$$$$#####^^^^^Banana&&&***)))@@@"

print("lstrip : ",val9.lstrip(),"end")
print("rstrip : ",val9.rstrip(),"end")
print("lstrip : ",val10.lstrip(".,$#^"),"end")
print("rstrip : ",val10.rstrip("&*)@"),"end")
print("strip : ",val9.strip(),"end")
print("strip : ",val10.strip(".,$#^&*)@"),"end")
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
# partition() and rpartition()
# Description : partition() : the method searches for a specified string, and splits the string into a tuple containing three elements
#               rpartition() : The method searches for the last occurrence of the specified string and returns a tuple with three elements
#               The first element contains the part before the string
#               The second element contains the specified string
#               The third element contains the part after the string

txt3 = "This is before the string match match_value This is after the string match ... match_value again"
print("partition  : ",txt3.partition("match_value"))
print("rpartition  : ",txt3.rpartition("match_value"))

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

#---------------------------------------------------------------------------------------------------------------------------------
# rfind() and rindex()
# Description : finds the last occurence of the specified value in a string
#               rfind() returns -1 if the value is not found whereas rindex() raises an exception if the value is not found.
# Syntax : string.rfind(value,start,end)
#          string.rindex(value,start,end)
#          value : (Required). The value to search for
#          start : (Optional), Where to start the search. Default is 0
#          end   : (Optional), Where to end the search, Default is end of string.

txt5 = "this is text ... this is text again ... text text text"

print("rfind : ",txt5.rfind("text"))
print("rfind : ",txt5.rfind("rext"))
print("rindex : ",txt5.rindex("text"))
# print("rindex : ",txt5.rindex("rext"))   # Commented because method returns an exception. UNCOMMENT TO RUN

#---------------------------------------------------------------------------------------------------------------------------------
# rsplit()
# Description : rsplit() :Splits a string into a list starting from the right end, using comma ',' followed by a space ' ' as the separator (Default separator)
#               YOU CAN ALSO SPECIFY A DIFFERENT SEPARATOR)
#               split() : Split a string into a list starting from the left, using comma ',' followed by a space ' ' as the separator (Default separator)
# Syntax  : string.rsplit(separator,maxsplit)
#           string.split(separator,maxsplit)
#            separator : (Optional).  Specifies the separator to use when splitting the string. By default any whitespace is a separator
#            MAXSPLIT  : (Optional). Specifies how many splits to do. Default value is -1 , which is "all occurrences"

text6 = "Apple, Banana, Orange, Pineapple, Cherry, Strawberry"
text7 = "Apple:Banana:Orange:Pineapple:Cherry:Strawberry"
text8 = "Apple_Banana_Orange_Pineapple_Cherry_Strawberry"

print("rsplit : ",text6.rsplit()) # With default separator
print("rsplit : ",text7.rsplit(":")) # With ":" as specified separator
print("rsplit : ",text8.rsplit("_",0)) # one occuernce in the output list
print("rsplit : ",text8.rsplit("_",1)) # two occuernce in the output list
print("rsplit : ",text8.rsplit("_",2)) # three occuernce in the output list
print("rsplit : ",text8.rsplit("_",3)) # four occuernce in the output list
print("rsplit : ",text8.rsplit("_",4)) # five occuernce in the output list
print("rsplit : ",text8.rsplit("_",5)) # six occuernce in the output list

print("split : ",text6.split()) # With default separator
print("split : ",text7.split(":")) # With ":" as specified separator
print("split : ",text8.split("_",0)) # one occuernce in the output list
print("split : ",text8.split("_",1)) # two occuernce in the output list
print("split : ",text8.split("_",2)) # three occuernce in the output list
print("split : ",text8.split("_",3)) # four occuernce in the output list
print("split : ",text8.split("_",4)) # five occuernce in the output list
print("split : ",text8.split("_",5)) # six occuernce in the output list

#---------------------------------------------------------------------------------------------------------------------------------
# splitlines()
# Description : The method splits a string into a list. The splitting is done at the linebreaks
# Syntax : string.splitlines(keeplinebreaks)
#          keeplinebreaks : (Optional). Specifies if the line breaks should be included (True) or not (False). [Default is False]

txt9 = "This is line 1 \n This is line 2 \n This is line 3 \n This is line 4"
print("splitlines : ",txt9)
print("splitlines : ",txt9.splitlines()) # This will return -> splitlines :  ['This is line 1 ', ' This is line 2 ', ' This is line 3 ', ' This is line 4']
print("splitlines : ",txt9.splitlines(True)) # This will return -> splitlines :  ['This is line 1 \n', ' This is line 2 \n', ' This is line 3 \n', ' This is line 4']

#---------------------------------------------------------------------------------------------------------------------------------
# swapcase()
# Description : Swaps lowercase to upper and uppercases to lower
# Syntax : string.swapcase()

txt10 = "TwItTeR sCrEeNsHoTs ArE nOt MeMeS 1a2B___@@123$$%"

print("swapcase : ",txt10.swapcase())

#---------------------------------------------------------------------------------------------------------------------------------
# title()
# Description : Converts the first character of each word in string to uppercase
# Syntax : string.title()

txt11 = "nothing is permanent in this material world"

print("title : ",txt11.title())

#---------------------------------------------------------------------------------------------------------------------------------
# zfill()
# Description : The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
#               If the value of the len parameter is less than the length of the string, no filling is done.
# Syntax : string.zfill(len)
#          len : (Required)

txt12 = "hello"
txt13 = "welcome to the jungle"
txt14 = "10.000"

print("zfill : ",txt12.zfill(10))
print("zfill : ",txt13.zfill(50))
print("zfill : ",txt14.zfill(20))

#===================================================================
#               CODE OUTPUT
#===================================================================
# using +ve and -ve indexes :  Hello W
# using +ve and -ve indexes :  o Worl
# capitalize :  Jayant yadav
# upper :  ALL CHARACTERS ARE LOWERCASE
# casefold :  jayant
# lower    :  jayant
# center :                        jayant                       end
# count :  4
# count :  3
# count :  2
# count :  2
# encode :  b'jayant'
# endswith :  True
# endswith :  True
# startswith :  True
# startswith :  True
# expandtabs :  Hello	World
# expandtabs :  Hello                                                                                               World
# find :  11
# find :  -1
# index : 11
# format :  Hi my name is Jayant and I love Coding
# join : ThisXYXisXYXoneXYXsentence
# join :  Thisisonesentence
# ljust :  Jayant               rocks
# ljust :  Jayantxxxxxxxxx
# rjust :                Jayant rocks
# rjust :  xxxxxxxxxJayant
# lstrip :  My name is Slim Shady           end
# rstrip :            My name is Slim Shady end
# lstrip :  Banana&&&***)))@@@ end
# rstrip :  .....,,,,,$$$$$#####^^^^^Banana end
# strip :  My name is Slim Shady end
# strip :  Banana end
# translate :  <class 'dict'> Hello Tam!
# translate :  Hello Joe!
# translate :  Thi i  ipl txt
# partition  :  ('This is before the string match ', 'match_value', ' This is after the string match ... match_value again')
# rpartition  :  ('This is before the string match match_value This is after the string match ... ', 'match_value', ' again')
# replace :  The quick brown tiger tiger tiger tiger tiger tiger tiger jumps over the lazy dog
# replace :  The quick brown wolf wolf wolf wolf fox fox fox jumps over the lazy dog
# rfind :  50
# rfind :  -1
# rindex :  50
# rsplit :  ['Apple,', 'Banana,', 'Orange,', 'Pineapple,', 'Cherry,', 'Strawberry']
# rsplit :  ['Apple', 'Banana', 'Orange', 'Pineapple', 'Cherry', 'Strawberry']
# rsplit :  ['Apple_Banana_Orange_Pineapple_Cherry_Strawberry']
# rsplit :  ['Apple_Banana_Orange_Pineapple_Cherry', 'Strawberry']
# rsplit :  ['Apple_Banana_Orange_Pineapple', 'Cherry', 'Strawberry']
# rsplit :  ['Apple_Banana_Orange', 'Pineapple', 'Cherry', 'Strawberry']
# rsplit :  ['Apple_Banana', 'Orange', 'Pineapple', 'Cherry', 'Strawberry']
# rsplit :  ['Apple', 'Banana', 'Orange', 'Pineapple', 'Cherry', 'Strawberry']
# split :  ['Apple,', 'Banana,', 'Orange,', 'Pineapple,', 'Cherry,', 'Strawberry']
# split :  ['Apple', 'Banana', 'Orange', 'Pineapple', 'Cherry', 'Strawberry']
# split :  ['Apple_Banana_Orange_Pineapple_Cherry_Strawberry']
# split :  ['Apple', 'Banana_Orange_Pineapple_Cherry_Strawberry']
# split :  ['Apple', 'Banana', 'Orange_Pineapple_Cherry_Strawberry']
# split :  ['Apple', 'Banana', 'Orange', 'Pineapple_Cherry_Strawberry']
# split :  ['Apple', 'Banana', 'Orange', 'Pineapple', 'Cherry_Strawberry']
# split :  ['Apple', 'Banana', 'Orange', 'Pineapple', 'Cherry', 'Strawberry']
# splitlines :  This is line 1
#  This is line 2
#  This is line 3
#  This is line 4
# splitlines :  ['This is line 1 ', ' This is line 2 ', ' This is line 3 ', ' This is line 4']
# splitlines :  ['This is line 1 \n', ' This is line 2 \n', ' This is line 3 \n', ' This is line 4']
# swapcase :  tWiTtEr ScReEnShOtS aRe NoT mEmEs 1A2b___@@123$$%
# title :  Nothing Is Permanent In This Material World
# zfill :  00000hello
# zfill :  00000000000000000000000000000welcome to the jungle
# zfill :  0000000000000010.000