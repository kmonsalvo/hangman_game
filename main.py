import random
import guessLetter as gl
import guessWord as gw
import drawMan as dm

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
        "newWord"     : word,       # word generated from list
        "numOfChar"   : rLength,    # number of characters in word
        "blankString" : newLine,    # "blank" word
        "blankChar"   : rLength*2,  # number of characters in the "blank" word
    }

    return wordAttributes

# Welcome Message
print("Welcome to the Hangman Game")
print("We are now going to generate a random word")
print("..... \n.... \n.... \n.... \n")

#Initialize
score = 10 #number of limbs on the hangman
newWord = wordGenerator() #generate the new word
blankWord = newWord["blankString"]


while (score > 0):
    blankWord = blankWord;
    print("Here is your word")
    print(blankWord)
    selIn = input("Do you want to try and guess the word [0] or select a letter [1]?")

    # Word or Letter?
    if (selIn == 0):
        pointDeduct = gw.init(newWord=newWord)
    else:
        pointDeduct = gl.init(newWord=newWord)

    # Deduct a point
    if (pointDeduct == True):
        score = score - 1
    else:
        score = score

    dm.draw(score=score)

print("LOSER")





