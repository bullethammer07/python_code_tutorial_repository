# Reading an already existing file in database
# here we choose : python_operators.py

f = open("python_operators.py")

# to know the current location of the file poiner 'f' you can use the tell() function. for eg.
# here we will print the file pointer before every readline

print(f.tell())
print("First line  : ", f.readline())
print(f.tell())
print("Second line : ", f.readline())
print(f.tell())
print("Third line  : ", f.readline())

# To reset the file pointer to another position you can use seek()
# for eg : here after reading some files we will use seek() to reset the file pointer back to 0 (start of file)

f.seek(0)
print("line now is : ", f.readline(), f.tell())

f.close()