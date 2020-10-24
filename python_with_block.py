# opening the dummy file

f = open("dummy_file_for fileops.txt")

print(f.readline(), f.tell())
print(f.readlines())

f.close()

# Syntax for opening file using 'with'
# This is equivalent to f = open(...)
#                       f.close()
# Thus with this method you do not need to close a file. It will take care of itself.

with open("dummy_file_for fileops.txt") as f:
    content = f.read()
    #print(content)
    cont_list = content.split("\n")
    print("num lines : ", len(cont_list))

    f.seek(0) # setting back file pointer to 0

    for val in range(len(cont_list)):
        print(val)
        print(f.readline())