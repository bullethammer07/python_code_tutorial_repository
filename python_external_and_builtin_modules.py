import random as randf # importing internal module 'random' as randf

for val in range(1, 10):
    random_num = randf.randint(1, 10)
    print(random_num)

#---------------------------------------
# Practicing with the 'random' library
#---------------------------------------

# Bookkeeping Functions
#  .seed()
#  .getstate()
#  .setstate()

# Functions for bytes
#  .randbytes

# Functions for Integers
#  .randrange()
#  .randint()
#  .getrandbits()

# Functions for Sequences
#  .choice()
#  .choices()
#  .shuffle()
#  .sample()

# Real valued distributions
#  .random()
#  .uniform()
#  .triangular()
#  .betavariate()
#  .expovariate()
#  .gammavariate()
#  .gauss()
#  .longnormvariate()
#  .vonmisesvariate()
#  .paretovariate()
#  .weibullvariate()

# Alternative Generator
#  .Random()
#  .SystemRandom()

for val in range(1, 20):
    print("randrange : ", randf.randrange(1, val))