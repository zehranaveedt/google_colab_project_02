# project 2: Guess the number game by computer

import random
def guess_the_number():
    """Project 2: Guess The Number Game By Computer."""
    number = random.randint(1, 100)
    guesses_left = 7

    #Welcome message
    print("Welcome to the number guessing game")
    print("I am thinking a number between 1 to 100")

    # loop generated
    while guesses_left > 0:
        print(f"\nYou have {guesses_left} guesses left.")
        try:
            guess = int(input("Take a guess for another number."))
        except ValueError:
            print("Invalid input: Please enter a number.")
            continue

    # guess the secret number
        if guess < number:
            print("Too Low number . Tell another!")
        elif guess > number:
            print("Too High number . Tell another!")
        else:
            print(f"Congratulation! you got the correct number in {7 - guesses_left +1 } tries.")
            return
        
        guesses_left -= 1
        print(f"\nYou ran out of guess . The number was {number}.")

guess_the_number()
