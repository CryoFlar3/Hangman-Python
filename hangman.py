import random
from words import words


ANSWER = "playstation"
HITS = ""
MISSES = ""

def get_random_word(words):
    global ANSWER 
    ANSWER = random.choice(words)
    return ANSWER

def Check_Input(userInput):
    userInput = str(userInput.lower())
    if userInput in HITS or userInput in MISSES :
        print("You already guessed that try again")
    else:
        return userInput

def apply_guess(userInput):
    global HITS
    global MISSES
    if userInput in ANSWER:
        HITS += userInput
    else:
        MISSES += userInput

def progress():
    progress = ""
    for letter in ANSWER:
        if letter in HITS:
            progress += letter
        else:
            progress += "-"
    return progress

def hangman():
    get_random_word(words)
    global HITS
    global MISSES
    print("Welcome to Hangman")
    while True:
        tries = 7 - len(MISSES)
        print("You have {} tries left".format(tries))
        print(progress())
        userProgress = progress()
        if ANSWER == userProgress:
            print("Congratulations")
            break
        if tries == 0:
            print("Bummer. The answer was {}".format(ANSWER))
            break
        userInput = str(input("Guess a letter: "))
        userInput = Check_Input(userInput)
        if userInput == None:
            continue
        apply_guess(userInput)
        
        
hangman()
print("Thank you for playing")