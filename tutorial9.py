#--------------------------------------------------------------
#             Python lists inbuilt functions
#--------------------------------------------------------------
# abs()              : Returns the absolute value of a secified number.
# all()              : Returns true if all items in an iterable are true, otherwise it returns False.
# any()              : Returns True if any item in an iterable are true, otherwise it returns False.
# ascii()            : Returns a readable version of any object (Strings, Tuples, Lists, etc). function will replace any non-ascii characters with escape characters.
#                      syntax: ascii(object)
# bin()              : Returns the binary version of a specified integer.
# bool()             : Returns the boolean value of a specified object (Any object, like String, List, Number etc).
# bytearray()        : Both bytearray() and bytes() returns a bytearray object.
# bytes()            : Both bytearray() and bytes() returns a bytearray object.
# callable()         : Returns True if the specified object is callable, otherwise it returns False.
# chr()              : Returns the character that represents the specified unicode.
# ord()              : Returns the number representing the unicode code of a specified character.
# compile()          : Returns the specified source as a code object, ready to be executed.
# eval()             : Evaluates the specified expression, if the expression is a legal Python statement, it will be executed.
# exec()             : The exec() function accepts large blocks of code, unlike the eval() function which only accepts a single expression

#----------------------------------------------------------------------------------------------------------------------
# abs()
# Description : returns the absolute value of a specified number
# Syntax : abs(n)
#          n : (Required). a number

print("\n")
x = abs(-7.21)
print("abs : ",x) # returns 7.21
y = abs(3+5j)
print("abs : ",y)

#----------------------------------------------------------------------------------------------------------------------
# all() and any()
# Description : all() : returns true if all items in an iterable are true, otherwise it returns false.
#               NOTE : if the iterable object is empty, all() function also returns true.
#               any() : returns True if any item in an iterable are true, otherwise it returns False.
#               NOTE : If the iterable object is empty, the any() function will return False.
# Syntax : all(iterable)
#          iterable : list, tuple, dictioary

print("\n")
list1 = ["Hi","my","name","is","Jayant"]
list2 = ["","","","",""]
list3 = ["Hi","my","name","",""]
list4 = [] # Empty list
print("all : ",all(list1)) # -> returns TRUE
print("all : ",all(list2)) # -> returns FALSE
print("all : ",all(list3)) # -> returns FALSE
print("all : ",all(list4)) # -> returns TRUE

print("any : ",any(list1)) # -> returns TRUE
print("any : ",any(list2)) # -> returns FALSE
print("any : ",any(list3)) # -> returns TRUE
print("any : ",any(list4)) # -> returns FALSE

#----------------------------------------------------------------------------------------------------------------------
# bin()
# Description : Returns the binary version of a specified integer.
#               The result will always start with the prefix 0b.
# Syntax : bin(n)
#          n : (Required). An Integer

print("\n")
print("bin : ",bin(69))

#----------------------------------------------------------------------------------------------------------------------
# bool()
# Description :  returns the boolean value of a specified object.
#                The object will always return True, unless:
#                The object is empty, like [], (), {}
#                The object is False
#                The object is 0
#                The object is N

empty_list = []
empty_tuple = ()
empty_array = {}
print("bool : ",bool(empty_list),bool(empty_tuple),bool(empty_array),bool("xyz"),bool(""))

#----------------------------------------------------------------------------------------------------------------------
# bytearray() and bytes()
# Descriptiom : both bytearray() and bytes() returns a bytearray object.
#               The difference between bytes() and bytearray() is that bytes() returns an object that cannot be modified, and bytearray() returns an object that can be modified.
# Syntax : bytearray(x,encoding,error)
#          bytes(x,encoding,error)
#          x : A source to use when creating a bytearray object.
#               NOTE : If it is an integer, An empty bytearray object of the specified size will be created.
#                    : If it is a string make sure you specify the encoding of the source.
#          encoding : The encoding of the string
#          error : specifies what to do if the encoding fails

print("\n")
print("bytearray : ",bytearray(10)) # -> Output is an empty bytearray of length 10 : bytearray :  bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
print("bytearray : ",bytearray("xyz","big5")) # specify the encoding in double quotes eg. "ascii" or "utf8" etc.

print("\n")
print("bytes : ",bytes(6))
print("bytes : ",bytes("xyz","big5"))

#----------------------------------------------------------------------------------------------------------------------
# callable()
# Description : Returns True if the specified object is callable, otherwise it returns False.
# Syntax : callable(object)
#          NOTE : A normal variable is not callable.

print("\n")
def func():
  print("Function call")

print("callable : ",callable(func)) # Returns true

var1 = 5;
print("callable : ",callable(var1))

#----------------------------------------------------------------------------------------------------------------------
# chr() and ord()
# Description : chr() Returns the character that represents the specified unicode.
#               ord() Returns the number representing the unicode code of a specified character.
# Syntax : chr(number)
#          number : An integer representing a valid Unicode code point
#          ord(character)
#          character : string, any character

print("\n")
print("chr : ",chr(97),chr(120),chr(36))
print("ord : ",ord("a"),ord("x"),ord("$"))

#----------------------------------------------------------------------------------------------------------------------
# eval() and exec()
# Description : eval() : Evaluates the specified expression, if the expression is a legal Python statement, it will be executed.
#                        In simple words, the eval function evaluates the “String” like a python expression and returns the result as an integer.
#                        The return value would be the result of the evaluated expression. Often the return type would be an integer.
#                        NOTE : eval() function which only accepts a single expression.
#                        Q : Where is the eval function mostly used?
#                        Ans : Eval function is mostly used in situations or applications which need to evaluate mathematical expressions.
#                              Also if the user wants to evaluate the string into code then can use eval function, because eval function evaluates the string expression and returns the integer as a result.
#                        Q : What is the difference between the input() and eval()?
#                        Ans : the input() takes the user input, but when the user enters an integer as an input the input function returns a string,
#                              but in the case of eval it will evaluate the returned value from a string to an integer.
#               exec() : Executes the specified Python code.
#                        NOTE : The exec() function accepts large blocks of code, unlike the eval() function which only accepts a single expression
# Syntax : eval(expression,globals,locals)
#          exec(expression,globals,locals)
#            expresion : A string, that will be evaluates as Python code.
#            globals : (Optional). A dictionary containing global variables.
#            locals : (Optional). A dictionary containing local variables.

print("\n")

#input_int = input("Enter Integer :: ")
# UNCOMMENT BELOW TO RUN
#print(input_int,type(input_int)) # the type will be returned as 'str' i.e string type
                                 # NOTE : If you enter an expression such as '10+10' it will not be evaluated as an interger with output 20.
                                 #        instead it will be returned as a string -> '10+10'

# UNCOMMENT BELOW TO RUN
#input_int2 = eval(input("Enter Integer :: "))
#print(input_int2,type(input_int2)) # the type will be returned as 'int' i.e integer type
                                   # NOTE : You can also enter an expression here like '10+20' and the output will be evaluated as 30 and as integer

# x = 'print(\"Hello World\")  print(\"This is text 1\")  print(\"this is text 2\")'
x = 'print("Hello world") | print("Jayant")' # multi print using eval (not recommended)
y = 'print("xyx")' # single print
z = 'val1 = 10  | print(val1)'
eval(y)

x1 = 'print("Hello world")\nprint("Jayant")' # Multi expressions
                                             # NOTE : do not put spaces before and after the \n as they can be treated as indents.
exec(x1)

#----------------------------------------------------------------------------------------------------------------------
# compile()
# Description :  returns the specified source as a code object, ready to be executed.
