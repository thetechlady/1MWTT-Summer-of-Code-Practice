

# Task: modify "a" for another name in my_dict (create new value pair)

my_dict = {"a": 35000, "b": 8000, "c": 450}

print(my_dict)

my_dict.pop("a")
my_dict["aaa"] = 35000

print(my_dict)



# Task: redo alice in wonderland frequency task and save it into a dict

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



# Task: create dict with personal details (creative and funny)

personal_dict = {
    "name": "Anne", 
    "age": "23",
    "profession": "student",
    "topic": "political science and network policy",
    "country": "germany"
}

personal_dict["fav_pet"] = "cat"
personal_dict["fav_book"] = "Harry Potter series"
personal_dict["fav_beer"] = "M&O Rostock"

print(personal_dict)




# Task: rewiew chat replay and instantiate student var for every dream shared

dream_dict = {}

dream_dict["Jessica"] = "work as a developer by the end of the year"
dream_dict["Deb Cupitt"] = "gender equity"
dream_dict["Virginia Balseiro"] = "moving to europe"
dream_dict["Christina Tarantio"] = "being an amazing developer"
dream_dict["Sacha Young"] = "french fries, to return to research"
dream_dict["Andreea Visanoui"] = "becoming an university teacher"
dream_dict["Bituin Callanta"] = "lessen gender wage gap"

print(dream_dict)




# Task: translate real world 1mwtt into student class code using 1mwtt landing page, decide on all attributes being meaninful

class Student():
    def __init__(self, firstname, lastname, mail, country_code, phone_number, github, membership):
        self. firstname = firstname
        self.lastname = lastname
        self.mail = mail
        self.country_code = country_code
        self.phone_number = phone_number
        self.github = github
        self.membership = membership
    