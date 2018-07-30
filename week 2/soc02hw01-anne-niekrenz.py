# Task: Calculate a table for each letter in the alphabet from a-z, 
# and count how many times each letter appears in alice_in_wonderland.txt

filename = "c:/users/anne/onedrive/code/alice_in_wonderland.txt"
file = open(filename, encoding="utf8")

raw = file.read()
print("The length of Alice in Wonderland is " + str(len(raw)) + " characters.")

from collections import Counter
counter = Counter(raw)

dict = {
    "a": counter["a"],
    "b": counter["b"],
    "c": counter["c"],
    "d": counter["d"],
    "e": counter["e"],
    "f": counter["f"],
    "g": counter["g"],
    "h": counter["h"],
    "i": counter["i"],
    "j": counter["j"],
    "k": counter["k"],
    "l": counter["l"],
    "m": counter["m"],
    "n": counter["n"],
    "o": counter["o"],
    "p": counter["p"],
    "q": counter["q"],
    "r": counter["r"],
    "s": counter["s"],
    "t": counter["t"],
    "u": counter["u"],
    "v": counter["v"],
    "w": counter["w"],
    "x": counter["x"],
    "y": counter["y"],
    "z": counter["z"]
}

print("From 163817 characters are in total: " + str(dict))
