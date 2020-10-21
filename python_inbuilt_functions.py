#--------------------------------------------------------------
#             Python inbuilt functions
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
# reversed()         : Function returns a reversed iterator object.
# len()             *: Function returns the number of items in an object. When the object is a string, the len() function returns the number of characters in the string.
# map()             *: Function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
# max()              : Function returns the item with the highest value, or the item with the highest value in an iterable.
# min()              : Function returns the item with the lowest value, or the item with the lowest value in an iterable.
# memoryview()      *: A memory view is a safe way to expose the buffer protocol in Python.
# object()           : Function returns a featureless object which is a base for all classes.
# print()            : Function prints the given object to the standard output device (screen) or to the text stream file.
# open()             : Function returns a file object which can used to read, write and modify the file.
# ord()              : Function returns an integer representing the Unicode character.
# pow()             *: Function computes the power of a number.
# range()            : Returns an immutable sequence of numbers between the given start integer to the stop integer.
# repr()             : Function returns a printable representation of the given object.
# round()            : Function returns a floating-point number rounded to the specified number of decimals.
# set()              : Creates a set in Python.
# slice()           *: Function returns a slice object that can use used to slice strings, lists, tuple etc.
# sorted()          *: Function sorts the elements of a given iterable in a specific order (either ascending or descending) and returns the sorted iterable as a list.
# sum()             *: Function adds the items of an iterable and returns the sum.
# tuple()            : Function creates a tuple object.
# type()             : Function returns the type of the specified object
# vars()            *: Function returns the __dict__ attribute of an object.
# zip()             *: Function returns a zip object, which is an iterator of tuples where the corresponding item in each passed iterator is paired together (one to one mapping fashion)
# oct()              : Function converts an integer into an octal string.
# str()             *: Function converts the specified value into a string.
# property()        *: Returns the property attribute.
# iter()            *: Function returns an iterator for the given object. creates an object which can be iterated one element at a time.
# next()            *: Function returns the next item from the iterator.
# super()           *: Returns a proxy object (temporary object of the superclass) that allows us to access methods of the base class.

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
compile_val = 'a = 10\nb = 20\nsum_val=a+b\nprint("compile : ",sum_val)'
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
# object()
# Description : Function returns a featureless object.
# Syntax : object()

print("\n")
obj_object = object()
print("object : ", type(obj_object))
print("object : ", dir(obj_object))

#----------------------------------------------------------------------------------------------------------------------
# print()
# Description : Function prints the given object to the standard output device (screen) or to the text stream file.
# Syntax : print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
#            objects : object to the printed. * indicates that there may be more than one object
#            sep : NOTE : objects are separated by sep. Default value: ' '
#            end : end is printed at last
#            file : must be an object with write(string) method. If omitted it, sys.stdout will be used which prints objects on the screen.
#            flush : If True, the stream is forcibly flushed. Default value: False

# We have a fair ides of how print works so we can skip with the usual

# below example is of writing to a file. We will comment this for now to avoid any creation of new files in the database
# UNCOMMENT BELOW TO RUN
# print("\n")
# source_file = open('python.txt', 'w')
# print('Hello World !!...', file = source_file)
# source_file.close()

#----------------------------------------------------------------------------------------------------------------------
# open()
# Description : Function returns a file object which can used to read, write and modify the file.
# Syntax : open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
#            file : The path and name of the file
#            mode : mode while opening a file. If not provided, it defaults to 'r' (open for reading in text mode). Available file modes are:
#                     'r'	Open a file for reading. (default)
#                     'w'	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
#                     'x'	Open a file for exclusive creation. If the file already exists, the operation fails.
#                     'a'	Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
#                     't'	Open in text mode. (default)
#                     'b'	Open in binary mode.
#                     '+'	Open a file for updating (reading and writing)
#            buffering : (optional). used for setting buffering policy
#            encoding : (optional). the encoding format
#            errors : (optional). string specifying how to handle encoding/decoding errors
#            newline : (optional). how newlines mode works (available values: None, ' ', '\n', 'r', and '\r\n'
#            closefd : (optional). must be True (default); if given otherwise, an exception will be raised
#            opener : (optional). a custom opener; must return an open file descriptor

# Return Value from open()
# The open() function returns a file object which can used to read, write and modify the file. If the file is not found, it raises the FileNotFoundError exception.

print("\n")
# Example 1: How to open a file in Python?

# opens test.text file of the current directory
# f = open("test.txt") # UNCOMMENT TO RUN : This will return an exceptionn as the file is not found
# specifying the full path
# f = open("C:/README.txt") # UNCOMMENT TO RUN : This will return an exceptionn as the file is not found

#----------------------------------------------------------------------------------------------------------------------
# ord()
# Description : function returns an integer representing the Unicode character.
# Syntax : ord(ch)
#           ch : a Unicode character

print("\n")
print("ord : ", ord('5'))    # 53
print("ord : ", ord('A'))    # 65
print("ord : ", ord('$'))    # 36

#----------------------------------------------------------------------------------------------------------------------
# pow()
# Description : Function computes the power of a number.
# Syntax : pow(x,y,z)
#            x : a number, the base
#            y : a number, the exponent
#            z : (Optional). a number, used for modulus

print("\n")
# Example 1: Python pow()

# positive x, positive y (x**y)
print("pow : ", pow(2, 2))    # 4
# negative x, positive y
print("pow : ", pow(-2, 2))    # 4
# positive x, negative y
print("pow : ", pow(2, -2))    # 0.25
# negative x, negative y
print("pow : ", pow(-2, -2))    # 0.25

# Example 2: pow() with three arguments (x**y) % z
print("pow : ", pow(7, 2, 5))    # 4

#----------------------------------------------------------------------------------------------------------------------
# range()
# Description : Returns an immutable sequence of numbers between the given start integer to the stop integer.
# Syntax : range(start,stop,step)
#            start : integer starting from which the sequence of integers is to be returned.
#            stop : stop - integer before which the sequence of integers is to be returned. # The range of integers ends at stop - 1.
#            step : (Optional). Integer value which determines the increment between each integer in the sequence.

# Return value from range()
# range() returns an immutable sequence object of numbers depending upon the definitions used:
#
# range(stop) :
#   1. Returns a sequence of numbers starting from 0 to stop - 1
#   2. Returns an empty sequence if stop is negative or 0.
#
# range(start, stop[, step]) :
#
# The return value is calculated by the following formula with the given constraints:
#
# r[n] = start + step*n (for both positive and negative step)
# where, n >=0 and r[n] < stop (for positive step)
# where, n >= 0 and r[n] > stop (for negative step)
#
#   1. (If no step) Step defaults to 1. Returns a sequence of numbers starting from start and ending at stop - 1.
#   2. (if step is zero) Raises a ValueError exception
#   3. (if step is non-zero) Checks if the value constraint is met and returns a sequence according to the formula
#      If it doesn't meet the value constraint, Empty sequence is returned.

print("\n")
# Example 1: How range works in Python?

# empty range
print("range : ", list(range(0)))
# using range(stop)
print("range : ", list(range(10)))
# using range(start, stop)
print("range : ", list(range(1, 10)))

# Example 2: Create a list of even number between the given numbers using range()
print("range : ", list(range(2, 14, 2)))

# Example 3: How range() works with negative step?
print("range : ", list(range(2, -14, -2)))

# value constraint not met
print("range : ", list(range(2, 14, -2)))

#----------------------------------------------------------------------------------------------------------------------
# repr()
# Description : Function returns a printable representation of the given object.
# Syntax : repr(obj)
#            obj : the object whose printable representation has to be returned

print("\n")
# Example 1: How repr() works in Python?

var = 'foo'
print("repr : ", repr(var))

# Example 2: Implement __repr__() for custom objects

class Person:
    name = 'Adam'

    def __repr__(self):
        return repr('Hello ' + self.name )

print("repr : ", repr(Person()))

#----------------------------------------------------------------------------------------------------------------------
# round()
# Description : Function returns a floating-point number rounded to the specified number of decimals.
# Syntax : round(number, ndigits)
#            number : the number to be rounded
#            ndigits : (optional). Number up to which the given number is rounded; defaults to 0

print("\n")
# Example 1: How round() works in Python?

# for integers
print("round : ", round(10))
# for floating point
print("round : ", round(10.7))
# even choice"round : ",
print("round : ", round(5.5))

# Example 2: Round a number to the given number of decimal places
print("round : ", round(2.665, 2))
print("round : ", round(2.675, 2))

#----------------------------------------------------------------------------------------------------------------------
# set()
# Description : creates a set in Python.
# Syntax : set(iterable)
#            iterable : (Optional). a sequence (string, tuple, etc.) or collection (set, dictionary, etc.) or an iterator object to be converted into a set.
#                       NOTE : an empty set is returned if no parameters are passed.
#                       NOTE : We cannot create empty sets using { } syntax as it creates an empty dictionary. To create an empty set, we use set().

print("\n")

# Example 1 : Create sets from string, tuple, list, and range

# empty set
print("set : ", set())
# from string
print("set : ", set('Python'))
# from tuple
print("set : ", set(('a', 'e', 'i', 'o', 'u')))
# from list
print("set : ", set(['a', 'e', 'i', 'o', 'u']))
# from range
print("set : ", set(range(5)))

# Example 2: Create sets from another set, dictionary and frozen set

# from set
print("set : ", set({'a', 'e', 'i', 'o', 'u'}))
# from dictionary
print("set : ", set({'a':1, 'e': 2, 'i':3, 'o':4, 'u':5}))
# set : ", "# from frozen set
frozen_set = frozenset(('a', 'e', 'i', 'o', 'u'))
print("set : ", set(frozen_set))

# Example 3: Create set() for a custom iterable object
class PrintNumber:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        self.num += 1
        return self.num

# print_num is an iterable
print_num = PrintNumber(5)
# creating a set
print("set : ", set(print_num))

#----------------------------------------------------------------------------------------------------------------------
# slice()
# Description : The slice object is used to slice a given sequence (string, bytes, tuple, list or range) or any object
#               which supports sequence protocol (implements __getitem__() and __len__() method).
# Syntax : slice(start, stop, step)
#            start : (optional) - Starting integer where the slicing of the object starts. Default to None if not provided.
#            stop : Integer until which the slicing takes place. The slicing stops at index stop -1 (last element).
#            step : (optional). Integer value which determines the increment between each index for slicing. Defaults to None if not provided.

print("\n")
# Example 1 : Creating a slice object for slicing

result1 = slice(3) # contains indices 0,1,2
result2 = slice(1,5,2) # contains indices 1,3
print("slice : ", result1)
print("slice : ", result2)

# Example 2 : Get substring using slice object

py_string = 'Python'
print("slice : ",py_string[result1]) # printing py_string using slice object 'result1'
print("slice : ",py_string[result2]) # printing py_string using slice object 'result2'

# Example 3 : Get sublist and sub-tuple

py_list = ['P', 'y', 't', 'h', 'o', 'n']
py_tuple = ('P', 'y', 't', 'h', 'o', 'n')

print("slice : ",py_list[result1]) # printing py_list using slice object 'result1'
print("slice : ",py_tuple[result2]) # printing py_tuple using slice object 'result2'

# Example 4 : Using indexing syntax for slicing
print("slice : ",py_string[0:3]) # contains indices 0,1,2
print("slice : ",py_string[1:5:2]) # contains indices 1,3

#----------------------------------------------------------------------------------------------------------------------
# sorted()
# Description : Function sorts the elements of a given iterable in a specific order (either ascending or descending) and returns the sorted iterable as a list.
# Syntax : sorted(iterable, key, reverse)
#            iterable : A sequence (string, tuple, list) or collection (set, dictionary, frozen set) or any other iterator.
#            key : (Optional). A function that serves as a key for the sort comparison. Defaults to None.
#            reverse : (Optional). If True, the sorted list is reversed (or sorted in descending order). Defaults to False if not provided.

print("\n")
# Example 1 : Sorting string, list and tuple

# vowels list
py_list = ['e', 'a', 'u', 'o', 'i']
print("sorted : ", sorted(py_list)) # sorts all the characters in the list alphabetically
# string
py_string = 'Python'
print("sorted : ",sorted(py_string)) # sorts all characters in the string alphabetically
# vowels tuple
py_tuple = ('e', 'a', 'u', 'o', 'i')
print("sorted : ", sorted(py_tuple)) # sorts all the characters in the tuple alphabetically

# Example 2 : Sort in descending order

# set
py_set = {'e', 'a', 'u', 'o', 'i'}
print("sorted : ", sorted(py_set, reverse=True)) # the set is reverse alphabetically sorted
# dictionary
py_dict = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}
print("sorted : ", sorted(py_dict, reverse=True)) # the dictionary is reverse apphabetically sorted
# frozen set
frozen_set = frozenset(('e', 'a', 'u', 'o', 'i'))  # the frozen set is reverse aplhabetically sorted
print("sorted : ", sorted(frozen_set, reverse=True))

# Example 3 : key Parameter in Python sorted() function
#             If you want your own implementation for sorting, sorted() also accepts a key function as an optional parameter.
#             Based on the returned value of the key function, you can sort the given iterable.

# sorting with ky=len : Here, len() is Python's in-built function to count the length of an object. The list is sorted based on the length of the element, from the lowest count to highest.
text = "This is a random string having words with different length sizes"
sorting_list = text.split() # converts text into a list
print("sorted : ", sorted(sorting_list, key=len)) # sorts the list by length

# Example 4 : Sort the list using sorted() having a key function
# take the second element for sort
def take_second(elem):
    return elem[1]

# random list
random_list = [(2, 2), (3, 4), (4, 1), (1, 3)]
# sort list with key
sort_list = sorted(random_list, key=take_second)
# print list
print('sorted : ', sort_list)

#----------------------------------------------------------------------------------------------------------------------
# sum()
# Description : Function adds the items of an iterable and returns the sum.
# Syntax : sum(iterable, start)
#            iterable : iterable (list, tuple, dict, etc). NOTE : The items of the iterable should be numbers.
#            start : this value is added to the sum of items of the iterable. The default value of start is 0 (if omitted)

print("\n")

ls1 = [1, 2, 3, 4, 5, 6]
list_sum = sum(ls1)

tp1 = (1, 2, 3, 4, 5, 6)
tup_sum = sum(tp1, 10) # adding a start value

print("sum : ", list_sum)
print("sum : ", tup_sum)

#----------------------------------------------------------------------------------------------------------------------
# tuple()
# Description : Function creates a tuple object.
# Syntax : tuple(iterable)
#            iterable : Required. A sequence, collection or an iterator object
#            NOTE : If the iterable is not passed to tuple(), the function returns an empty tuple.

print("\n")

tup1 = tuple()
print('tuple : ', tup1)

# creating a tuple from a list
tup2 = tuple([1, 4, 6])
print('tuple : ', tup2)

# creating a tuple from a string
tup3 = tuple('Python')
print('tuple : ', tup3)

# creating a tuple from a dictionary
tup4 = tuple({1: 'one', 2: 'two'})
print('tuple : ', tup4)

# creating a tuple from a list
tup5 = tuple(['Python', 'programming', 'is', 'fun'])
print('tuple : ', tup5)

#----------------------------------------------------------------------------------------------------------------------
# type()
# Description : Function returns the type of the specified object
# Syntax : type(object, bases, dict)
#            object : (Required). If only one parameter is specified, the type() function returns the type of this object
#            bases : (Optional). Specifies the base classes
#            dict : (Optional). Specifies the namespace with the definition for the class

# Just pass any variable to type() without any 'bases' and 'dict' and it will return the object type, SIMPLE

# IMPT : Creating a 'type' object

print("\n")
o1 = type('X', (object,), dict(a='Foo', b=12))
print("type : ", type(o1))
print("type : ", vars(o1))

class test:
    a = 'Foo'
    b = 12

o2 = type('Y', (test,), dict(a='Foo', b=12))
print("type : ", type(o2))
print("type : ", vars(o2))

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
# vars()
# Description : Function returns the __dic__ attribute of an object.
#               The __dict__ attribute is a dictionary containing the object's changeable attributes.
# Syntax : vars(object)
#            object : Any object with a __dict__attribute

print("\n")
class dict_class:
  name = "Jayant"
  age = 27
  country = "India"

dict_class_inst = dict_class()

#print("vars : ",vars(list_1_l4)) # UNCOMMENT TO RUN : This will create an excption as the list passed does not have an __dict__ attribute
print("vars : ",vars(dict_class_inst)) # returns {}
print("vars : ",vars(dict_class)) # returns the complete attribute

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

print("\n")
# Example 1: Create attribute with getter, setter, and deleter
class Person_class:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('Getting name')
        return self._name

    def set_name(self, value):
        print('Setting name to ' + value)
        self._name = value

    def del_name(self):
        print('Deleting name')
        del self._name

    # Set property to use get_name, set_name
    # and del_name methods
    name = property(get_name, set_name, del_name, 'Name property')

p = Person_class('Adam')

print(p.name)
p.name = 'John'
del p.name

#----------------------------------------------------------------------------------------------------------------------
# property()
# Description : Returns the property attribute.
#               returns the property attribute from the given getter, setter, and deleter.
#               NOTE : If no arguments are given, property() returns a base property attribute that doesn't contain any getter, setter or deleter.
#               note : If doc isn't provided, property() takes the docstring of the getter function.
# Syntax : property(fget=None, fset=None, fdel=None, doc=None)
#            fget : (optional). Function for getting the attribute value. Defaults to None.
#            fset :(optional). Function for setting the attribute value. Defaults to None.
#            fdel :(optional). Function for deleting the attribute value. Defaults to None.
#            doc :(optional). A string that contains the documentation (docstring) for the attribute. Defaults to None.

print("\n")

# Example 1: Create attribute with getter, setter, and deleter

# Here, _name is used as the private variable for storing the name of Person.
#
# We also set:
#
# a getter method get_name() to get the name of the person,
# a setter method set_name() to set the name of the person,
# a deleter method del_name() to delete the name of the person.
# Now, we set a new property attribute name by calling the property() method.
#
# As shown in the program, referencing p.name internally calls get_name() as getter, set_name() as setter and del_name() as deleter through the printed output present inside the methods.

class Person_class2:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('Getting name')
        return self._name

    def set_name(self, value):
        print('Setting name to ' + value)
        self._name = value

    def del_name(self):
        print('Deleting name')
        del self._name

    # Set property to use get_name, set_name
    # and del_name methods
    name = property(get_name, set_name, del_name, 'Name property')

print("property :: ")
p = Person_class2('Adam')
print(p.name)
p.name = 'John'
print(p.name)
del p.name
# print(p.name) # UNCOMMENT TO RUN : This will return an exception as p.name attribute has been deleted

# Example 2 : Using @property decorator
# Instead of using property(), you can use the Python decorator @property to assign the getter, setter, and deleter.

class Person_class3:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('Getting name')
        return self._name

    @name.setter
    def name(self, value):
        print('Setting name to ' + value)
        self._name = value

    @name.deleter
    def name(self):
        print('Deleting name')
        del self._name

print("property :: ")
pp = Person_class3('Adam')
print('The name is:', pp.name)
pp.name = 'John'
print(pp.name)
del pp.name
# print(p.name) # UNCOMMENT TO RUN : This will return an exception as p.name attribute has been deleted

#----------------------------------------------------------------------------------------------------------------------
# iter()
# Description : Function creates an object which can be iterated one element at a time.
#               NOTE : These objects are useful when coupled with loops like for loop, while loop.
# Syntax : iter(object,sentinel)
#            object - object whose iterator has to be created (can be sets, tuples, etc.)
#            sentinel (optional) - special value that is used to represent the end of a sequence

# Return value from iter()
#  1. The iter() function returns an iterator object for the given object.
#  2. If the user-defined object doesn't implement __iter__(), and __next__() or __getitem()__, the TypeError exception is raised.
#  3. If the sentinel parameter is also provided, iter() returns an iterator until the sentinel character isn't found.

print("\n")

# Example 1: Working of Python iter()

# list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']
vowels_iter = iter(vowels)

print("iter : ", next(vowels_iter))    # 'a'
print("iter : ", next(vowels_iter))    # 'e'
print("iter : ", next(vowels_iter))    # 'i'
print("iter : ", next(vowels_iter))    # 'o'
print("iter : ", next(vowels_iter))    # 'u'

# Example 2: iter() for custom objects

class PrintNumber:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        self.num += 1
        return self.num

print("\n")
print_num = PrintNumber(3)

print_num_iter = iter(print_num)
print("iter : ", next(print_num_iter))  # 1
print("iter : ", next(print_num_iter))  # 2
print("iter : ", next(print_num_iter))  # 3

# raises StopIteration
# print("iter : ", next(print_num_iter)) # UNCOMMENT TO RUN : This will generate an exception

# Example 3: iter() with sentinel parameter

# Here, we have implemented a custom iterable object without a StopIteration condition.
# However, we can use the iter() method with the sentinel parameter to stop the iteration.
# If the value returned from __next__() is equal to sentinel, StopIteration will be raised, otherwise, the value will be returned.

class DoubleIt:

    def __init__(self):
        self.start = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.start *= 2
        return self.start

    __call__ = __next__

my_iter = iter(DoubleIt(), 16)

print("\n")
for x in my_iter:
    print("iter : ", x)

#----------------------------------------------------------------------------------------------------------------------
# next()
# Description : Function returns the next item from the iterator.
# Syntax : next(iterator, default)
#            iterator : next() retrieves next item from the iterator
#            default : (optional). this value is returned if the iterator is exhausted (there is no next item)

# Return Value from next
# 1. The next() function returns the next item from the iterator.
# 2. If the iterator is exhausted, it returns the default value passed as an argument.
# 3. If the default parameter is omitted and the iterator is exhausted, it raises StopIteration exception.

print("\n")

# Example 1: Get the next item
random_iter = [5, 9, 'cat']

# converting the list to an iterator
random_iterator = iter(random_iter)
print("next : ", random_iterator)

# Output: 5
print("next : ", next(random_iterator))
# Output: 9
print("next : ", next(random_iterator))
# Output: 'cat'
print("next : ", next(random_iterator))
# This will raise Error
# iterator is exhausted
# print("next : ", next(random_iterator)) # UNCOMMENT TO RUN : This will generate an exception because we tried to get the next item when no next item was available (iterator is exhausted).
                                          # In such cases, you can give a default value as the second parameter.

# Example 2: Passing default value to next()

random_iter2 = [5, 9]

# converting the list to an iterator
random_iterator2 = iter(random_iter2)

print("\n")
# Output: 5
print("next : ", next(random_iterator2, '-1'))
# Output: 9
print("next : ", next(random_iterator2, '-1'))
# random_iterator is exhausted
# Output: '-1'
print("next : ", next(random_iterator2, '-1'))
print("next : ", next(random_iterator2, '-1'))
print("next : ", next(random_iterator2, '-1'))

#----------------------------------------------------------------------------------------------------------------------
# super()
# Description : Returns a proxy object (temporary object of the superclass) that allows us to access methods of the base class.
#               In Python, super() has two major use cases:
#                1. Allows us to avoid using the base class name explicitly
#                2. Working with Multiple Inheritance
# Syntax : super()

print("\n")
print("super :: ")
# Example 1: super() with Single Inheritance
# In the case of single inheritance, it allows us to refer base class by super().

# Here, we called the __init__() method of the Mammal class (from the Dog class) using code
# super().__init__('Dog')
# instead of
# Mammal.__init__(self, 'Dog')

class Mammal(object):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')

class Dog(Mammal):
    def __init__(self):
        print('Dog has four legs.')
        super().__init__('Dog')

d1 = Dog()

# Example 2: super() with Multiple Inheritance
class Animal:
    def __init__(self, Animal):
        print(Animal, 'is an animal.');

class Mammal2(Animal):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
        super().__init__(mammalName)

class NonWingedMammal(Mammal2):
    def __init__(self, NonWingedMammal):
        print(NonWingedMammal, "can't fly.")
        super().__init__(NonWingedMammal)

class NonMarineMammal(Mammal2):
    def __init__(self, NonMarineMammal):
        print(NonMarineMammal, "can't swim.")
        super().__init__(NonMarineMammal)

class Dog(NonMarineMammal, NonWingedMammal):
    def __init__(self):
        print('Dog has 4 legs.');
        super().__init__('Dog')

print("\n")
print("super multi inheritance :: ")
d = Dog()

print("\n")
print("super multi inheritance :: ")
bat = NonMarineMammal('Bat')

# ================================================================================================
#                                OUTPUT
# ================================================================================================
# abs :  7.21
# abs :  5.830951894845301
#
#
# all :  True
# all :  False
# all :  False
# all :  True
# any :  True
# any :  False
# any :  True
# any :  False
#
#
# bin :  0b1000101
# bool :  False False False True False
#
#
# bytearray :  bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
# bytearray :  bytearray(b'xyz')
#
#
# bytes :  b'\x00\x00\x00\x00\x00\x00'
# bytes :  b'xyz'
#
#
# callable :  True
# callable :  False
#
#
# chr :  a x $
# ord :  97 120 36
#
#
# xyx
# Hello world
# Jayant
#
#
# compile :  30
#
#
# complex :  (3+4j) <class 'complex'>
#
#
# Jayant
# getattr :  India
# hasattr :  True False
# setattr :  Jayant Yadav
#
#
# dict :  {'name': 'Jayant', 'age': '27', 'country': 'India'}
#
#
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
#
#
# divmod :  (16, 4)
#
#
# list :  ['apple', 'banana', 'orange', 'strawberry']
#
#
# enumerate :  [(0, 'apple'), (1, 'banana'), (2, 'orange')]
#
#
# filter :  [18, 24, 32]
#
#
# float :  5.0 3.145987
#
#
# format :  ff
# format :  11111111
#
#
# frozenset :  frozenset({'cherry', 'banana', 'apple'})
#
#
# globals :  {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001E63DBC3760>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:\\Users\\Bullet-HammeR\\PycharmProjects\\first_proj\\tutorial9.py', '__cached__': None, 'x': 'print("Hello world") | print("Jayant")', 'y': 'print("xyx")', 'list1': ['Hi', 'my', 'name', 'is', 'Jayant'], 'list2': ['', '', '', '', ''], 'list3': ['Hi', 'my', 'name', '', ''], 'list4': [], 'empty_list': [], 'empty_tuple': (), 'empty_array': {}, 'func': <function func at 0x000001E63DBBE040>, 'var1': 5, 'z': 'val1 = 10  | print(val1)', 'x1': 'print("Hello world")\nprint("Jayant")', 'compile_val': 'a = 10\nb = 20\nsum_val=a+b\nprint("compile : ",sum_val)', 'code_object': <code object <module> at 0x000001E63E3850E0, file "sum_string", line 1>, 'a': 10, 'b': 20, 'sum_val': 30, 'complex_val': (3+4j), 'mydata': <class '__main__.mydata'>, 'getat': 'India', 'hasat1': True, 'hasat2': False, 'mydict': {'name': 'Jayant', 'age': '27', 'country': 'India'}, 'dmod_var': (16, 4), 'list_var': ['apple', 'banana', 'orange', 'strawberry'], 'tup1': ('apple', 'banana', 'orange'), 'enum1': <enumerate object at 0x000001E63E3879C0>, 'ages': [5, 12, 17, 18, 24, 32], 'filter_func': <function filter_func at 0x000001E63E11B430>, 'adults': <filter object at 0x000001E63E13B6D0>, 'float1': 5.0, 'float2': 3.145987, 'frozen_list': ['apple', 'banana', 'cherry'], 'var2': frozenset({'cherry', 'banana', 'apple'}), 'var3': {...}, 'var3l': {...}}
# locals :  {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001E63DBC3760>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:\\Users\\Bullet-HammeR\\PycharmProjects\\first_proj\\tutorial9.py', '__cached__': None, 'x': 'print("Hello world") | print("Jayant")', 'y': 'print("xyx")', 'list1': ['Hi', 'my', 'name', 'is', 'Jayant'], 'list2': ['', '', '', '', ''], 'list3': ['Hi', 'my', 'name', '', ''], 'list4': [], 'empty_list': [], 'empty_tuple': (), 'empty_array': {}, 'func': <function func at 0x000001E63DBBE040>, 'var1': 5, 'z': 'val1 = 10  | print(val1)', 'x1': 'print("Hello world")\nprint("Jayant")', 'compile_val': 'a = 10\nb = 20\nsum_val=a+b\nprint("compile : ",sum_val)', 'code_object': <code object <module> at 0x000001E63E3850E0, file "sum_string", line 1>, 'a': 10, 'b': 20, 'sum_val': 30, 'complex_val': (3+4j), 'mydata': <class '__main__.mydata'>, 'getat': 'India', 'hasat1': True, 'hasat2': False, 'mydict': {'name': 'Jayant', 'age': '27', 'country': 'India'}, 'dmod_var': (16, 4), 'list_var': ['apple', 'banana', 'orange', 'strawberry'], 'tup1': ('apple', 'banana', 'orange'), 'enum1': <enumerate object at 0x000001E63E3879C0>, 'ages': [5, 12, 17, 18, 24, 32], 'filter_func': <function filter_func at 0x000001E63E11B430>, 'adults': <filter object at 0x000001E63E13B6D0>, 'float1': 5.0, 'float2': 3.145987, 'frozen_list': ['apple', 'banana', 'cherry'], 'var2': frozenset({'cherry', 'banana', 'apple'}), 'var3': {...}, 'var3l': {...}}
#
#
# hex :  0xff
#
#
# id :  2088397994736
#
#
# int :  255
# int :  255
# int :  255
#
#
# isinstance :  True
# isinstance :  False
# isinstance :  True
#
#
# issubclass :  True
# issubclass :  False
#
#
# reversed :  t
# reversed :  n
# reversed :  a
# reversed :  y
# reversed :  a
# reversed :  j
#
#
# len :  4
# len :  5
# len :  16
# len :  6
#
#
# map :  [4, 2, 2, 5, 7]
#
#
# max :  7
# min :  1
# max :  ffffff
# min :  a
#
#
# memoryview :  65
# memoryview :  b'AB'
# memoryview :  [65, 66, 67]
#
#
# object :  <class 'object'>
# object :  ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
#
#
#
#
# ord :  53
# ord :  65
# ord :  36
#
#
# pow :  4
# pow :  4
# pow :  0.25
# pow :  0.25
# pow :  4
#
#
# range :  []
# range :  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# range :  [1, 2, 3, 4, 5, 6, 7, 8, 9]
# range :  [2, 4, 6, 8, 10, 12]
# range :  [2, 0, -2, -4, -6, -8, -10, -12]
# range :  []
#
#
# repr :  'foo'
# repr :  'Hello Adam'
#
#
# round :  10
# round :  11
# round :  6
# round :  2.67
# round :  2.67
#
#
# set :  set()
# set :  {'t', 'y', 'n', 'o', 'h', 'P'}
# set :  {'i', 'u', 'a', 'o', 'e'}
# set :  {'i', 'u', 'a', 'o', 'e'}
# set :  {0, 1, 2, 3, 4}
# set :  {'a', 'o', 'e', 'i', 'u'}
# set :  {'a', 'o', 'e', 'i', 'u'}
# set :  {'a', 'o', 'e', 'i', 'u'}
# set :  {1, 2, 3, 4, 5}
#
#
# slice :  slice(None, 3, None)
# slice :  slice(1, 5, 2)
# slice :  Pyt
# slice :  yh
# slice :  ['P', 'y', 't']
# slice :  ('y', 'h')
# slice :  Pyt
# slice :  yh
#
#
# sorted :  ['a', 'e', 'i', 'o', 'u']
# sorted :  ['P', 'h', 'n', 'o', 't', 'y']
# sorted :  ['a', 'e', 'i', 'o', 'u']
# sorted :  ['u', 'o', 'i', 'e', 'a']
# sorted :  ['u', 'o', 'i', 'e', 'a']
# sorted :  ['u', 'o', 'i', 'e', 'a']
# sorted :  ['a', 'is', 'This', 'with', 'words', 'sizes', 'random', 'string', 'having', 'length', 'different']
# sorted :  [(4, 1), (2, 2), (1, 3), (3, 4)]
#
#
# sum :  21
# sum :  31
#
#
# tuple :  ()
# tuple :  (1, 4, 6)
# tuple :  ('P', 'y', 't', 'h', 'o', 'n')
# tuple :  (1, 2)
# tuple :  ('Python', 'programming', 'is', 'fun')
#
#
# type :  <class 'type'>
# type :  {'a': 'Foo', 'b': 12, '__module__': '__main__', '__dict__': <attribute '__dict__' of 'X' objects>, '__weakref__': <attribute '__weakref__' of 'X' objects>, '__doc__': None}
# type :  <class 'type'>
# type :  {'a': 'Foo', 'b': 12, '__module__': '__main__', '__doc__': None}
#
#
# zip :  [('This', 'This'), ('is', 'is'), ('list', 'list'), ('one', 'one')]
# zip :  [('This', 'This', 'This'), ('is', 'is', 'is'), ('list', 'list', 'list'), ('one', 'one', 'one')]
# zip :  [('This', 'This'), ('is', 'is'), ('list', 'another'), ('one', 'list')]
# zip :  [('This', 'This'), ('is', 'is'), ('list', 'tuple'), ('one', 'one')]
#
#
# vars :  {}
# vars :  {'__module__': '__main__', 'name': 'Jayant', 'age': 27, 'country': 'India', '__dict__': <attribute '__dict__' of 'dict_class' objects>, '__weakref__': <attribute '__weakref__' of 'dict_class' objects>, '__doc__': None}
#
#
# oct :  0o377
#
#
# str :  123
# str :  ['This', 'is', 'list']
# str :  ('This', 'is', 'tuple')
# str :  <__main__.test_class object at 0x000001E63E13BB80>
#
#
# Getting name
# Adam
# Setting name to John
# Deleting name
#
#
# property ::
# Getting name
# Adam
# Setting name to John
# Getting name
# John
# Deleting name
# property ::
# Getting name
# The name is: Adam
# Setting name to John
# Getting name
# John
# Deleting name
#
#
# iter :  a
# iter :  e
# iter :  i
# iter :  o
# iter :  u
#
#
# iter :  1
# iter :  2
# iter :  3
#
#
# iter :  2
# iter :  4
# iter :  8
#
#
# next :  <list_iterator object at 0x000001E63E13B9A0>
# next :  5
# next :  9
# next :  cat
#
#
# next :  5
# next :  9
# next :  -1
# next :  -1
# next :  -1
#
#
# super ::
# Dog has four legs.
# Dog is a warm-blooded animal.
#
#
# super multi inheritance ::
# Dog has 4 legs.
# Dog can't swim.
# Dog can't fly.
# Dog is a warm-blooded animal.
# Dog is an animal.
#
#
# super multi inheritance ::
# Bat can't swim.
# Bat is a warm-blooded animal.
# Bat is an animal.