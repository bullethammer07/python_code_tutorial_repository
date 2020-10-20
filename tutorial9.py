#--------------------------------------------------------------
#             Python lists inbuilt functions
#--------------------------------------------------------------
# abs()              : Returns the absolute value of a secified number.
# all()              : Returns true if all items in an iterable are true, otherwise it returns False.
# any()              : Returns True if any item in an iterable are true, otherwise it returns False.
# ascii()            : Returns a readable version of any object (Strings, Tuples, Lists, etc). function will replace any non-ascii characters with escape characters.
# bin()              : Returns the binary version of a specified integer.
# bool()             : Returns the boolean value of a specified object (Any object, like String, List, Number etc).
# bytearray()        : Both bytearray() and bytes() returns a bytearray object.
# bytes()            : Both bytearray() and bytes() returns a bytearray object.
# callable()         : Returns True if the specified object is callable, otherwise it returns False.
# chr()              : Returns the character that represents the specified unicode.
# ord()              : Returns the number representing the unicode code of a specified character.
# eval()            *: Evaluates the specified expression, if the expression is a legal Python statement, it will be executed.
# exec()            *: The exec() function accepts large blocks of code, unlike the eval() function which only accepts a single expression
# compile()         *: Returns the specified source as a code object, ready to be executed.
# complex()          : Returns a complex number for the real and img value passed
# delattr()          : Function will delete the specified attribute from the specified object
# getattr()          : Function returns the value of the specified attribute from the specified object.
# hasattr()          : Function returns True if the specified object has the specified attribute, otherwise False.
# setattr()          : Function sets the value of the specified attribute of the specified object.
# dict()            *: Creates a dictionary containing information.
# dir()              : Function returns all properties and methods of the specified object, without the values.
# divmod()           : Function returns a tuple containing the quotient  and the remainder when argument1 (divident) is divided by argument2 (divisor).
# list()            *: Returns a list
# enumerate()        : Function takes a collection (e.g. a tuple) and returns it as an enumerate object.
# filter()          *: Function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
# float()           *: Function converts the specified value into a floating point number.
# format()           : Function formats a specified value into a specified format.
# frozenset()        : Function returns an unchangeable frozenset object (which is like a set object, only unchangeable).
# globals()          : Function returns the global symbol table as a dictionary.
# locals()           : Function returns the local symbol table as a dictionary. A symbol table contains necessary information about the current program.
# hash()             : Not Specified
# help()             : Not Specified
# hex()             *: Function converts the specified number into a hexadecimal value.
# id()               : Function returns a unique id for the specified object.
# input()            : <Already Known>
# int()             *: Function converts the specified value into an integer number.
# isinstance()      *: Function returns True if the specified object is of the specified type, otherwise False.
# issubclass()      *: Function returns True if the specified object is a subclass of the specified object, otherwise False.
# iter()            *: TODO : [Need to Understand Better ... Skipping for now] Function creates an object which can be iterated one element at a time.
# reversed()         : Function returns a reversed iterator object.
# len()             *: Function returns the number of items in an object. When the object is a string, the len() function returns the number of characters in the string.
# map()             *: Function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
# max()              : Function returns the item with the highest value, or the item with the highest value in an iterable.
# min()              : Function returns the item with the lowest value, or the item with the lowest value in an iterable.
# memoryview()      *: A memory view is a safe way to expose the buffer protocol in Python.
# next()
# object()
# open()
# ord()
# pow()
# print()
# property()
# range()
# repr()
# round()
# set()
# slice()
# sorted()
# sum()
# super()
# tuple()
# type()
# vars()
# zip()             *: Function returns a zip object, which is an iterator of tuples where the corresponding item in each passed iterator is paired together (one to one mapping fashion)
# oct()              : Function converts an integer into an octal string.
# str()             *: Function converts the specified value into a string.

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
# Description :  Returns the specified source as a code object, ready to be executed.
#                The compile() method returns a Python code object from the source (normal string, a byte string, or an AST object).
#                The code object returned by compile() method can later be called using methods like: exec() and eval() which will execute dynamically generated Python code.
# Syntax : compile(source,filename,mode,flags=0,dont_inherit=False,optimize=-1)
#            source : a normal string, a byte string, or an AST object
#            filename : file from which the code was read. If it wasn't read from a file, you can give a name yourself
#            mode : Either 'exec' or 'eval' or 'single'.
#              eval : accepts only a single expression
#              exec : It can take a code block that has Python statements, class and functions, and so on.
#              single :  if it consists of a single interactive statement.
#            flags : (optional). controls which future statements affect the compilation of the source. Default Value: 0
#            dont_inherit : (optional). controls which future statements affect the compilation of the source. Default Value: False
#            optimize : (optional). optimization level of the compiler. Default value -1.

print("\n")
compile_val = 'a = 10\nb = 20\nsum=a+b\nprint("compile : ",sum)'
code_object = compile(compile_val, 'sum_string', 'exec')

exec(code_object)

#----------------------------------------------------------------------------------------------------------------------
# complex()
# Description : Returns a complex number by specifying a real number and an imaginary number.
# Syntax : complex(real,iamginary)
#            real : (Required). represents real part of the number

print("\n")
complex_val = complex(3,4)
print("complex : ",complex_val,type(complex_val))

#----------------------------------------------------------------------------------------------------------------------
# delattr() getattr() hasattr() setattr()
# Description : delattr() :  function will delete the specified attribute from the specified object.
# Syntax : delattr(object,attribute) / getattr(object,attribute) / hasattr(object,attribute)
#            object : (Required). An Object
#            attribute : (Required). The name of the attrubute you want to remove/get/has.
#          setattr(object,attribute,value)
#            object : (Required). An Object
#            attribute : (Required). The name of the attrubute you want to set
#            value : (Required). The value you want to give the specified attribute

class mydata:
    name = "Jayant"
    age = 27
    country = "India"

print("\n")
print(mydata.name)
delattr(mydata,"name")
#print("delattr : ",mydata.name) # This will return an error as attribute "name" has been removed : UNCOMMENT TO RUN

getat = getattr(mydata,"country")
print("getattr : ",getat)

hasat1 = hasattr(mydata,"age")
hasat2 = hasattr(mydata,"sex")
print("hasattr : ",hasat1,hasat2)

setattr(mydata,"name","Jayant Yadav")
print("setattr : ",mydata.name) # This will return name as "Jayant Yadav" instead of "Jayant"

#----------------------------------------------------------------------------------------------------------------------
# dict()
# Description : creates a dictionary (array) containing information specified
# Syntax : dict(keyword arguments)
#            keyword arguments : (Required).  As many keyword arguments you like, separated by comma: key = value, key = value ...

print("\n")
mydict = dict(name = "Jayant", age = "27", country = "India")
print("dict : ",mydict)

#----------------------------------------------------------------------------------------------------------------------
# dir()
# Description : function returns all properties and methods of the specified object, without the values.
# Syntax : dir(object)

print("\n")
print(dir(mydict))

#----------------------------------------------------------------------------------------------------------------------
# divmod()
# Description : Function returns a tuple containing the quotient  and the remainder when argument1 (divident) is divided by argument2 (divisor).
# Syntax : divmod(divident, divisor)
#            divident : A Number. The number you want to divide
#            divisor : A Number. The number you want to divide with

print("\n")
dmod_var = divmod(100,6)
print("divmod : ",dmod_var)

#----------------------------------------------------------------------------------------------------------------------
# list()
# Description : Creates a list object
# Syntax : list(iterable)
#            iterable : (Required). A sequence, collection or an iterator object.

print("\n")
list_var = list(("apple","banana","orange","strawberry"))
print("list : ",list_var)

#----------------------------------------------------------------------------------------------------------------------
# enumerate()
# Description : Function takes a collection (e.g. a tuple) and returns it as an enumerate object.
#               The enumerate() function adds a counter as the key of the enumerate object.
# Syntax : enumerate(iterable,start)
#            iterable : An iterable object
#            start : (Optional). A Number. Defining the start number of the enumerate object. Default 0

print("\n")
tup1 = ("apple", "banana", "orange")
enum1 = enumerate(tup1)
print("enumerate : ", list(enum1)) # enum1 is an iterator object and can be printed as a list

#----------------------------------------------------------------------------------------------------------------------
# filter()
# Description : Function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
# Syntax : filter(function,iterable)
#            function : A function to be run for each item in the iterable
#            iterable : the iterable to be filtered.

print("\n")
ages = [5, 12, 17, 18, 24, 32]

def filter_func(xy):
    if xy < 18:
        return False
    else:
        return True

adults = filter(filter_func,ages) # adults is an iterator object and can be print using list()
print("filter : ",list(adults)) # adults is printed using list()

#----------------------------------------------------------------------------------------------------------------------
# float()
# Description : function converts the specified value into a floating point number.
# Syntax : float(value)
#            value : A number or a string that can be converted into a floating point number

print("\n")
float1 = float(5)
float2 = float("3.145987")
print("float : ",float1, float2)

#----------------------------------------------------------------------------------------------------------------------
# format()
# Description : Function formats a specified value into a specified format.
# Syntax : format(value, format)
#            value : A value of any format.
#            format : The format you want to format the value into.
#                     Legal values:
#                     '<' - Left aligns the result (within the available space)
#                     '>' - Right aligns the result (within the available space)
#                     '^' - Center aligns the result (within the available space)
#                     '=' - Places the sign to the left most position
#                     '+' - Use a plus sign to indicate if the result is positive or negative
#                     '-' - Use a minus sign for negative values only
#                     ' ' - Use a leading space for positive numbers
#                     ',' - Use a comma as a thousand separator
#                     '_' - Use a underscore as a thousand separator
#                    *'b' - Binary format
#                    *'c' - Converts the value into the corresponding unicode character
#                    *'d' - Decimal format
#                    *'e' - Scientific format, with a lower case e
#                    *'E' - Scientific format, with an upper case E
#                    *'f' - Fix point number format
#                    *'F' - Fix point number format, upper case
#                     'g' - General format
#                     'G' - General format (using a upper case E for scientific notations)
#                    *'o' - Octal format
#                    *'x' - Hex format, lower case
#                    *'X' - Hex format, upper case
#                     'n' - Number format
#                     '%' - Percentage format

print("\n")
print("format : ",format(255, 'x'))
print("format : ",format(255, 'b'))

#----------------------------------------------------------------------------------------------------------------------
# frozenset()
# Description : Function returns an unchangeable frozenset object (which is like a set object, only unchangeable).
# Syntax : frozenset(iterable)
#            iterable : An iterable object, like list, set, tuple etc.

print("\n")
frozen_list = ['apple', 'banana', 'cherry']
var2 = frozenset(frozen_list)
print("frozenset : ",var2)

# trying to set some value in a frozenset
# var2[1] = "strawberry" # UNCOMMENT TO RUN , as it will generate an exception.

#----------------------------------------------------------------------------------------------------------------------
# globals() and locals()
# Description : globals() : Function returns the global symbol table as a dictionary.
#               locals() : Function returns the local symbol table as a dictionary.
# Syntax : globals()
#          locals()

print("\n")
var3 = globals()
var3l = locals()
print("globals : ",var3)
print("locals : ", var3l)

#----------------------------------------------------------------------------------------------------------------------
# hex()
# Description : Function converts the specified number into a hexadecimal value.
#               the returned string always starts with prefix 0x
# Syntax : hex(number)
#            number : An Integer

print("\n")
var4 = hex(255)
print("hex : ", var4)

#----------------------------------------------------------------------------------------------------------------------
# id()
# Description : Function returns a unique id for the specified object. All objects in Python has its own unique id.
#               The id is assigned to the object when it is created. The id is the object's memory address, and will be different for each time you run the program.
#               (except for some object that has a constant unique id, like integers from -5 to 256)
# Syntax : id(object)
#            object : Any object, String, Number, List, Class etc.

print("\n")
print("id : ",id(var4)) # printing id of var4

#----------------------------------------------------------------------------------------------------------------------
# int()
# Description : Function converts the specified value into an integer number.
# Syntax : int(value,base)
#            value : A number or a string that can be converted into an integer number
#            base : A number representing the number format. Default value: 10

print("\n")
var5 = int("11111111",2) # binary value
var6 = int("377",8) # octal value
var7 = int("ff",16) # hexadecimal value

print("int : ", var5)
print("int : ", var6)
print("int : ", var7)

#----------------------------------------------------------------------------------------------------------------------
# isinstance()
# Description : Function returns True if the specified object is of the specified type, otherwise False.
# Syntax : isinstance(object,type)
#            object : (Required). An object
#            type : A type or a class, or a tuple of types and/or classes

print("\n")
var8 = isinstance("Hello", (float, int, str, list, dict, tuple)) # checking if object is part of from a tuple of types , this will return as TRUE
print("isinstance : ",var8)

var9 = isinstance("Hello",int)
print("isinstance : ", var9) # this will return false

class myObj:
  name = "John"

class_obj = myObj()

var10 = isinstance(class_obj, myObj)
print("isinstance : ", var10) # this will return true

#----------------------------------------------------------------------------------------------------------------------
# issubclass()
# Description : Function returns True if the specified object is a subclass of the specified object, otherwise False.
# Syntax : issubclass(object, parentclass)
#            object : (Required). An Object
#            parentclass : A class object, or a tuple of class objects

print("\n")
class myAge:
  age = 36

class myNameAge(myAge):
  name = "John"
  age = myAge

print("issubclass : ",issubclass(myNameAge, myAge)) # Will return true as myNameAge is extended form myAge
print("issubclass : ",issubclass(myAge, myNameAge)) # Will return false as myAge is not extended form myNameAge

#----------------------------------------------------------------------------------------------------------------------
# iter()
# Description : Function returns an iterator object.
#               NOTE : If the user-defined object doesn't implement __iter__(), and __next__() or __getitem()__, the TypeError exception is raised.
# Syntax : iter(object, sentinel)
#            object : (Required).  object whose iterator has to be created (can be sets, tuples, etc.)
#            sentinel : (Optional). special value that is used to represent the end of a sequence
#            NOTE : If the sentinel parameter is also provided, iter() returns an iterator until the sentinel character isn't found.

#----------------------------------------------------------------------------------------------------------------------
# reversed()
# Description : Function returns a reversed iterator object.
# Syntax : reversed(sequence)
#            sequence : (Required). Any iterable object.

print("\n")
alph = ["j", "a", "y", "a", "n", "t"]
ralph = reversed(alph)
for x in ralph:
  print("reversed : ", x)

#----------------------------------------------------------------------------------------------------------------------
# len()
# Description : Function returns the number of items in an object.
#               When the object is a string, the len() function returns the number of characters in the string.
# Syntax : len(object)
#            object : (Required).  An object. Must be a sequence or a collection

obj1 = ["This", "is", "a", "list"]
obj2 = ("This", "is", "a", "simple", "tuple")
obj3 = "This is a String"

class test_class:
    name = "Jayant"
    surname = "Yadav"
    age = "27"
    company = "xyz_firm"
    emp_id = "12345A"
    desig = "engg"

    def __len__(self):
        return 6

class_inst = test_class()

print("\n")
print("len : ",len(obj1)) # returns number of items in list obj1
print("len : ",len(obj2)) # returns number of items in tuple obj2
print("len : ",len(obj3)) # returns length of string obj3
print("len : ",len(class_inst)) # NOTE : we have implemented function __len__ in class 'test_class' due to which we are able to get an output
                                # however if we did not implement the function we would get an exception -> TypeError: object of type 'test_class' has no len()

#----------------------------------------------------------------------------------------------------------------------
# map()
# Description : Function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
# Syntax : map(function, iterables)
#            function : (Required). The function to execute for each item
#            iterable : (Required). A sequence, collection or an iterator object. You can send as many iterables as you like, just make sure the function has one parameter for each iterable.

print("\n")

map_arr = ["This", "is", "an", "array", "example"]
def length_func(n):
    return len(n)

map_var = map(length_func, map_arr) # creates an iterator object
print("map : ",list(map_var)) # used 'list()' to print the iterator object

#----------------------------------------------------------------------------------------------------------------------
# max() and min()
# Description : max() : Function returns the item with the highest value, or the item with the highest value in an iterable. If the values are strings, an alphabetically comparison is done.
#               min() : Function returns the item with the lowest value, or the item with the lowest value in an iterable. If the values are strings, an alphabetically comparison is done.
# Syntax : max(n1, n2, n3, ...) or max(iterable)
#          min(n1, n2, n3, ...) or min(iterable)
#            n1, n2, n3, ... : One or more items to compare
#            iterable : An iterable, with one or more items to compare

print("\n")

# specifying list or array directly
maxval = max(1,2,3,4,5,6,7)
minval = min(1,2,3,4,5,6,7)
print("max : ", maxval)
print("min : ", minval)

str_arr = ["a", "bb", "ccc", "dddd", "eeeee", "ffffff"]
strmax = max(str_arr)
strmin = min(str_arr)
print("max : ", strmax) # returns the string of max length
print("min : ", strmin) # returns the string of min length

num_str_arr = ["a", "bb", "ccc", "dddd", "eeeee", "ffffff" ,1 , 2 , 3]
#num_str_maxval = max(num_str_arr) # UNCOMMENT TO RUN
#num_str_minval = min(num_str_arr) # UNCOMMENT TO RUN
#print("max : ", num_str_maxval) # UNCOMMENT TO RUN : This will return an error as the list has both 'str' and 'int' -> TypeError: '>' not supported between instances of 'int' and 'str'
#print("max : ", num_str_minval) # UNCOMMENT TO RUN : This will return an error as the list has both 'str' and 'int' -> TypeError: '>' not supported between instances of 'int' and 'str'

#----------------------------------------------------------------------------------------------------------------------
# memoryview()
#
# Before we get into what memory views are, we need to first understand about Python's buffer protocol.
#
# Python Buffer Protocol :
# 1. The buffer protocol provides a way to access the internal data of an object. This internal data is a memory array or a buffer.
# 2. The buffer protocol allows one object to expose its internal data (buffers) and the other to access those buffers without intermediate copying.
# 3. This protocol is only accessible to us at the C-API level and not using our normal codebase.
# 4. So, in order to expose the same protocol to the normal Python codebase, memory views are present.
#
# Q : What is a memory view ?.
# Ans : A memory view is a safe way to expose the buffer protocol in Python.
#       It allows you to access the internal buffers of an object by creating a memory view object.
#
# Q : Why buffer protocol and memory views are important?
# Ans : We need to remember that whenever we perform some action on an object (call a function of an object, slice an array), Python needs to create a copy of the object.
#       If we have large data to work with (eg. binary data of an image), we would unnecessarily create copies of huge chunks of data, which serves almost no use.
#       Using the buffer protocol, we can give another object access to use/modify the large data without copying it. This makes the program use less memory and increases the execution speed.
#
# Description : A memory view is a safe way to expose the buffer protocol in Python.
# Syntax : memoryview(obj)
#            obj : A Bytes object or a Bytearray object.

print("\n")
# creating a bytearray for a random string
random_byte_array = bytearray('ABC', 'utf-8')
memview = memoryview(random_byte_array) # Here, we created a memory view object 'memview' from the byte array random_byte_array.

# accessing the 0th location
print("memoryview : ", memview[0]) # we accessed the 'memview's 0th index, 'A', and printed it (which gives the ASCII value - 65).
print("memoryview : ", bytes(memview[0:2])) # we accessed the 'memview's indices from 0 and 1, 'AB' , and converted them into bytes.
print("memoryview : ", list(memview[0:3])) # we accessed all indices of 'memview' and converted it to a list. Since internally bytearray stores ASCII value for the alphabets,
                                           # the output is a list of ASCII values of A, B, and C.

#----------------------------------------------------------------------------------------------------------------------
# zip()
# Description : Function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are
#               paired together etc.
#               NOTE : If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.
#               NOTE : zip() returns an iterator object
# Syntax : zip(iterator1, iterator2, iterator3 ...
#            iterator1, iterator2, iterator3 ... : 	Iterator objects that will be joined together

print("\n")
list_1_l4 = ["This", "is", "list", "one"]
list_2_l5 = ["This", "is", "list", "number", "two"]
list_3_l6 = ["This", "is", "another", "list", "number", "three"]
tuple_1_l4 = ("This", "is", "tuple", "one")
tuple_2_l5 = ("This", "is", "tuple", "number", "two")
tuple_3_l6 = ("This", "is", "another", "tuple", "number", "three")

# joining list1 length4 to itself
print("zip : ", list(zip(list_1_l4, list_1_l4))) # using list since zip returns an iterator object
# joining list1 length4 to itself thrice
print("zip : ", list(zip(list_1_l4, list_1_l4, list_1_l4))) # We can zip a list with a tuple and vice versa
# joining two lists with diff length
print("zip : ", list(zip(list_1_l4, list_3_l6))) # the smaller list determines the length of the resulting list

# joining a list and a tuple
print("zip : ", list(zip(list_1_l4, tuple_1_l4)))

#----------------------------------------------------------------------------------------------------------------------
# oct()
# Description : Function converts an integer into an octal string.
#               Octal strings in Python are prefixed with 0o.
# Syntax : oct(int)
#            int : An integer number

print("\n")
oct_val = oct(255)
print("oct : ", oct_val)

#----------------------------------------------------------------------------------------------------------------------
# str()
# Description : Function converts the specified value into a string.
# Syntax : str(object, encoding, errors)
#            object : Any object. Specifies the object to convert into a string
#            encoding : The encoding of the object. Default is UTF-8
#            errors : Specifies what to do if the decoding fails

print("\n")
ob1 = 123
ob2 = ["This", "is", "list"]
ob3 = ("This", "is", "tuple")

class_inst2 = test_class() # making object of test_class made earlier

print("str : ", str(ob1))
print("str : ", str(ob2)) # a list also gets converted to string
print("str : ", str(ob3)) # a tuple also gets converted to string
print("str : ", str(class_inst2)) # Need to analyze


#----------------------------------------------------------------------------------------------------------------------
# ()
# Description :
# Syntax :