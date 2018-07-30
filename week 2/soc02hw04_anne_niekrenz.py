

# Task: install pip, NLTK, Anaconda and Jupyter Notebook


import nltk

from nltk.book import *

# text2
# text1.concordance("monstrous")




# Task: Exercise #5 from http://www.nltk.org/book/ch01.html 
# Compare the lexical diversity scores for humor and romance fiction in 1.1. 
# Which genre is more lexically diverse?


def lexical_diversity(text):
    return len(set(text)) / len(text)

def percentage(count, total):
    return 100 * count / total

print("Lexical diversity for Moby Dick by Herman Melville: " + str(lexical_diversity(text1)))