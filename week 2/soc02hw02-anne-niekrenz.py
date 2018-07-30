

# Task: fixing the A-Z and a-z ASCII code

for i in range(65,65+26):
    print(str(i) + " stands for: " + str(chr(i)))
for i in range(97,97+26):
    print(str(i) + " stands for: " + str(chr(i)))


# Task: make a function that asks the user for a message and turns it into a list of ASCII numbers

print("Please enter your message: ")
message = input()

print("Your encrypted message is:")

for crypt in message:
     print(ord(crypt))


# Task: Write a function that prints out all elements of the board
# Write a function that prints out all elements in reverse

o = "water"
M = "land"

world = [
 [o,o,o,o,o,o,o,o,o,o,o],
 [o,o,o,o,M,M,o,o,o,o,o],
 [o,o,o,o,o,o,o,o,M,M,o],
 [o,o,o,M,o,o,o,o,o,M,o],
 [o,o,o,M,o,M,M,o,o,o,o],
 [o,o,o,o,M,M,M,M,o,o,o],
 [o,o,o,M,M,M,M,M,M,M,o],
 [o,o,o,M,M,o,M,M,M,o,o],
 [o,o,o,o,o,o,M,M,o,o,o],
 [o,M,o,o,o,M,o,o,o,o,o],
 [o,o,o,o,o,o,o,o,o,o,o]
 ]

for list in world:
    print(list) 

for list in reversed(world):
    print(list)


# Task: Write a function that generates an n x n sized board with either land or water chosen randomly

import random

random.shuffle(world)

for sublist in world:
    random.shuffle(sublist)

print(world)