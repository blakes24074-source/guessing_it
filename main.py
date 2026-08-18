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

import random



def validate_guess (inp):
    try:
        return int(inp)
    except:
        return False

def mainloop ():
    while (True):
        ans = random.randint(1, 100)
        guesses = 1 # add redundancy, we only need to add 1 after each incorrect guess to reduce operations
        while (True):
            guess = validate_guess(input("Guess: "))

            if (guess == ans):
                print("Correct guess! Guess count:",guesses)
                break

            print("Incorrect!")
            guesses += 1

mainloop()