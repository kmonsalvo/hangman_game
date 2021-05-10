# 10 total points
#   O
#--- ---
#   |
#  / \
# 1 point per character
def draw(score):
    if (score == 0):
        print("          ")
        print("          ")
        print("          ")
        print("          ")
    if (score == 1):
        print("     O    ")
        print("          ")
        print("          ")
        print("          ")
    if (score == 2):
        print("     O    ")
        print(" -        ")
        print("          ")
        print("          ")
    if (score == 3):
        print("     O    ")
        print(" --       ")
        print("          ")
        print("          ")
    if (score == 4):
        print("     O    ")
        print(" ---      ")
        print("          ")
        print("          ")
    if (score == 5):
        print("     O    ")
        print(" ---  -   ")
        print("          ")
        print("          ")
    if (score == 6):
        print("     O    ")
        print(" ---  --  ")
        print("          ")
        print("          ")
    if (score == 7):
        print("     O    ")
        print(" ---  --- ")
        print("          ")
        print("          ")
    if (score == 8):
        print("     O    ")
        print(" ---  --- ")
        print("     |    ")
        print("          ")
    if (score == 9):
        print("     O    ")
        print(" ---  --- ")
        print("     |    ")
        print("    /     ")
    if (score == 10):
        print("     O    ")
        print(" ---  --- ")
        print("     |    ")
        print("    / \   ")

