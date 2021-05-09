import random

def wordGenerator():
    f = open("words.txt","rt") # open txt file
    lines=f.readlines() # read all lines
    lineNum = random.randint(1,2999) # generate random number
    word = lines[lineNum] # extract random word
    rLength = len(word)-1 #real length og word (characters)
    maxLine0 = "_ _ _ _ _ " #10 characters per blank
    maxLineSum = maxLine0 * 4 #40 character blank string (no word in list should be over 40 characters
    newLine = maxLineSum[0:(rLength*2-1)] #create blank string to present to user

    wordAttributes = {
        "newWord"     : word,     # word generated from list
        "numOfChar"   : rLength,  # number of characters in word
        "blankString" : newLine,  # blank string
    }

    return wordAttributes

# Welcome Message
print("Welcome to the Hangman Game")
print("We are now going to generate a random word")
print("..... \n.... \n.... \n.... \n")

newWord = wordGenerator()
print(newWord["newWord"])
print(newWord["numOfChar"])
print(newWord["blankString"])
