"""
    main.py
        - who could guess what this file is?
    iteration 01
    loop
        - intro - ask name
        - mainloop
            - generate correct answer
            - loop until player answer = correct answer, give hints if wrong
        - do not end mainloop
    
"""

import random # used primarily for random.randint()

"""
    CONFIG
        * configuration for this file

    "min_ans" : int -- minimum number that can be the correct answer
    "max_ans" : int -- maximum number that can be the correct answer
    "name_validation"
        - "min_len" : int -- minimum length of a name acceptable
        - "max_len" : int -- maximum length of a name acceptable
        - "allow_int" : boolean -- whether or not to allow numbers in a name (ie "bob123" would not pass if "allow_int" = False, but would pass if "allow_int" = True)
"""
CONFIG = {
    "min_ans" : 1,
    "max_ans" : 100,
    "name_validation" : {
        "min_len" : 2,
        "max_len" : 15,
        "allow_int" : False,
    }
}

"""
    validate_name()
        * checks if the supplied string (name) is between two sets of lengths, and
        * whether or not it has numbers in it

@param {str} name - the string to validate

@return {boolean} - whether or not the string is valid
"""
def validate_name (name : str):
    if (len(name) < CONFIG["name_validation"]["min_len"] or len(name) > CONFIG["name_validation"]["max_len"]):
        return False
    if CONFIG["name_validation"]["allow_int"]:
        return True
    return name.isalpha()


def intro():
    print("Welcome to numberguesser!")
    while (True):
        name = input("Enter your name: ")
        if validate_name(name):
            break
        print("Invalid name!")
    print("\n\n\n\n")

"""
    validate_guess()
        * check if the string provided can be casted to an integer
        * return false if unable to cast

@param {str} inp -- inputted string to be casted and checked

@return {int || bool} -- int if successfully casted, False if failed
"""
def validate_guess (inp : str):
    try:
        return int(inp)
    except:
        return False

"""
    mainloop()
        * The main loop function
        * Effectively what will be run first

    !! will loop eternally, do not run code afterward !!
"""
def mainloop ():
    while (True):
        ans = random.randint(1, 100)
        guesses = 1 # add redundancy, we only need to add 1 after each incorrect guess to reduce operations
        while (True):
            guess = validate_guess(input("Guess: "))

            if (guess == ans):
                print("Correct guess! Guess count:",guesses,"\n\n")
                break

            print("Incorrect! ", end="") # redundancy!
            if (guess > ans):
                print("Guess is too high!")
            else:
                print("Guess is too low!")
            guesses += 1

if (__name__ == "__main__"):
    intro()
    mainloop()