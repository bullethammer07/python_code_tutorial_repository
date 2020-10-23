# --------------------------------------------------------------
#             Python file inbuilt methods
# --------------------------------------------------------------
# close()         : Closes an opened file. It has no effect if the file is already closed.
# detach()        : Separates the underlying binary buffer from the TextIOBase and returns it.
# fileno()        : Returns an integer number (file descriptor) of the file.
# flush()         : Flushes the write buffer of the file stream.
# isatty()        : Returns True if the file stream is interactive.
# read(n)         : Reads at most n characters from the file. Reads till end of file if it is negative or None.
# readable()      : Returns True if the file stream can be read from.
# readline(n=-1)  : Reads and returns one line from the file. Reads in at most n bytes if specified.
# readlines(n=-1) : Reads and returns a list of lines from the file. Reads in at most n bytes/characters if specified.
# seek(offset,from=SEEK_SET)   : Changes the file position to offset bytes, in reference to from (start, current, end).
# seekable()      : Returns True if the file stream supports random access.
# tell()          : Returns the current file location.
# truncate()      : Resizes the file stream to size bytes. If size is not specified, resizes to current location.
# writable()      : Returns True if the file stream can be written to.
# write()         : Writes the string s to the file and returns the number of characters written.
# writelines()    : Writes a list of lines to the file.

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# When we want to read from or write to a file, we need to open it first.
# When we are done, it needs to be closed so that the resources that are tied with the file are freed.
# Hence, in Python, a file operation takes place in the following order:
#   1. Open a file
#   2. Read or write (perform operation)
#   3. Close the file

#------------------------------
# Creating text files in Python
#------------------------------

# With Python you can create a .text files (<filename>.txt) by using below code:
#   We declared the variable f to open a file named temp.txt.
#   Open takes 2 arguments, the file that we want to open and a string that represents the kinds of permission or operation we want to do on the file.
#   Here, we used "w" letter in our argument, which indicates write and will create a file if it does not exist in library
#   + sign indicates both read and write

file = open("temp.txt", "w+")

# writing some data
for i in range(10):
     file.write("This is line %d\n" % (i+1))

file.close()

#---------------------------------
# deleting all contents of a file
#---------------------------------

# print("Deleting all contents of file")
# file = open("temp.txt", 'r+')
# file.truncate(0) # deleting all contents of file


#--------------------------
# Opening files in Python
#--------------------------
# Python has a built-in open() function to open a file. This function returns a file object, also called a handle, as it is used to read or modify the file accordingly.

# f = open("random.txt") # open file in current directory
# f = open("C:/Python38/README.txt")  # specifying full path

# We can specify the mode while opening a file. In mode, we specify whether we want to read r, write w or append a to the file.
# We can also specify if we want to open the file in text mode or binary mode.

# The default is reading in text mode. In this mode, we get strings when reading from the file.

# On the other hand, binary mode returns bytes and this is the mode to be used when dealing with non-text files like images or executable files.

# Mode	Description
#  r	  Opens a file for reading. (default)
#  w	  Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
#  x	  Opens a file for exclusive creation. If the file already exists, the operation fails.
#  a	  Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
#  t	  Opens in text mode. (default)
#  b	  Opens in binary mode.
#  +	  Opens a file for updating (reading and writing)

# Syntax : eg
#   f = open("test.txt", mode='r', encoding='utf-8')

#--------------------------
# closing files in Python
#--------------------------

# When we are done with performing operations on the file, we need to properly close the file.
# Closing a file will free up the resources that were tied with the file. It is done using the close() method available in Python.
# Python has a garbage collector to clean up unreferenced objects but we must not rely on it to close the file.

# example of opening and closing a file
# f = open("test.txt", encoding = 'utf-8')
# f.close()

# This method is not entirely safe. If an exception occurs when we are performing some operation with the file, the code exits without closing the file.
# A safer way is to use a try...finally block.
#
# try:
#    f = open("test.txt", encoding = 'utf-8')
#    # perform file operations
# finally:
#    f.close()

# This way, we are guaranteeing that the file is properly closed even if an exception is raised that causes program flow to stop.

# NOTE : The best way to close a file is by using the with statement. This ensures that the file is closed when the block inside the with statement is exited.
#        We don't need to explicitly call the close() method. It is done internally.

# eg.
#   with open("test.txt", encoding = 'utf-8') as f:
#    # perform file operations