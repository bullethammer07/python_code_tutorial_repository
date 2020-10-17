str = "Hello World"

print(str[0:7])
print(str[-7:-1])

# -------------------------------------------------

# capitalize()
val = "jayant"
print(val.capitalize()) # To convert the first letter to capitals

# casefold
val1 = "JAYANT"
print(val1.casefold()) # To convert string to lowercase

# center()
val2 = "jayant"
print(val2.center(50)) # Prints the string in the centre of specified number of blank spaces

# count()
val3 = "what what what what WHAT WHAT WHAT WHY WHY when when"
print(val3.count("what")) # Counts the number of occurences of a specified value in a string
print(val3.count("WHAT"))
print(val3.count("WHY"))
print(val3.count("when"))

# encode()
val4 = "jayant"
print(val4.encode()) # The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
                     # Refer :  https://docs.python.org/2.4/lib/standard-encodings.html for a link of all encoding types
"""
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
expandtabs()
Syntax : string.expandtabs(tabsize)
Description : Replaces any tabs in the string with the specified number of whitespaces
"""
val5 = "Hello\tWorld"
print(val5)
print(val5.expandtabs(100))

"""
find()
Syntax : string.find(value)
Description : Returns the index where the match(if found) starts in the string.
"""
val6 =