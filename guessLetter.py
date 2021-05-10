def init(newWord):
    letterIn = input("Type your guess (1 letter or character): ") #ask for a letter and capture input
    #loop through string to see if letter is in string
    word = newWord["newWord"]
    length = newWord["numOfChar"]
    error = 0

    for i in word:
        if letterIn == word[i]:
            index = i
            print(i)
        else:
            error = error + 1

    if (error > 0):
        pointDeduct = True
        print("Your guess us incorrect!")
    else:
        pointDeduct = False
        print("Your guess is correct!")

    return pointDeduct
