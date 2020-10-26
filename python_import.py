import sys

paths = sys.path
print(paths) # This will return list of all path python searches files to import modules from

# Importing contents from other files
# for eg. we will port function 'my_function4' from the file 'python_args_kwargs.py' present in the projetc
#         for that we can do as below

from python_args_kwargs import my_function4

my_function4("Stupid value")

# To import a complete file you can use as below : (module is present in the project)

import python_args_kwargs

print("The name is : ", __name__) # This will return as : The name is :  __main__
                                  # only when this file is executed on run.