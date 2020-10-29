# Dictionaries are basically key-value pairs

# Dictionaries are made with curly braces
# below d1 is an empty dictionary

d1 = {}
print(type(d1))
print(d1)

d2 = {1: "ABC", 2: "PQR", 3: "XYZ"}
print(d2[1]) # Indexing using number , since key is numeric

d3 = {"name1": "Jayant", "name2": "Amit", "name3": "Nikhil"}
print(d3["name2"]) # Indexing using string , since key is string

# A dictionary item can also be a dictionary. for eg
d4 = {"player1":{"Bench": 100, "Squat": 140, "Deadlift":200} ,
      "player2":{"Bench": 120, "Squat": 120, "Deadlift":180}}
print(type(d4["player1"]), d4["player1"])
print(type(d4["player2"]), d4["player2"])
# Printing Player 2's Deadlift
print(d4["player1"]["Squat"]) # Querying individual element of dictonary inside a dictionary

#-----------------------------------------------------------------------

# Updating existing dictionary by adding new element
# here we will add new player to d4


player3 = {"player3":{"Bench": 50, "Squat": 50, "Deadlift":80}}
d4.update(player3) # updating d4 by adding another player 'player 3'
# printing player3 profile
print(d4["player3"])
# printing complete dictionary
print(d4)

#------------------------------------------------------------------------

# deleting a player from the dictionary

del d4["player1"]
print(d4) # this will delete player1 from the dictionary