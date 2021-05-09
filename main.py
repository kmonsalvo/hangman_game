import random

def blankLine(stringIn, lengthIn):


def wordGenerator():
    f = open("words.txt","rt") # open txt file
    lines=f.readlines() # read all lines
    lineNum = random.randint(1,2999) # generate random number
    word = lines[lineNum] # extract random word
    rLength = len(newWord)-1
    blankLine = "_ "

    attributes = {
        newWord     : word, # word generated
        numOfChar   : rLength,  # determine number of character in word
        blankString :
    }

    print("#DEBUG# Word: {newWord}".format(newWord=newWord))
    print("#DEBUG# Word Length: {rLength}".format(rLength=rLength))
    print(".....")
    print(".....")
    print(".....")
    print(".....")


# Welcome Message
print("Welcome to the Hangman Game")
print("We are now going to generate a random word")
print("..... \n .... \n")

newWord = wordGenerator()
