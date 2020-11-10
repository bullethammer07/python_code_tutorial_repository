#---------------------------------
#   Python Set Comprehensions     
#---------------------------------

# NOTE : Set Comprehensions use : []

list1 = [1, 1, 1, 1, 2, 2, 2, 3, 4, 5, 6, 6, 7, 7]

# making a set using set comprehensions
set1 = { val for val in list1 }

print("created set is : ", set1)