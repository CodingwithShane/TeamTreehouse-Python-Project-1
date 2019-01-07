"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    # Declaring variable outside of loop to NOT reset it when game restarts
    top_score = "0"
    # While True the game keeps playing
    while True:
        number = random.randint(1, 101)
        attempts = 0

        # I have used the guess art from http://guess.ascii.uk/ however the box is mine.
        print("--------------------------------------------------")
        print("|                                                 |")
        print("|    .d88b. 888  888 .d88b. .d8888b .d8888b       |")
        print("|   d88P\"88b888  888d8P  Y8b88K     88K           |")
        print("|   888  888888  88888888888\"Y8888b.\"Y8888b.      |")
        print("|   Y88b 888Y88b 888Y8b.         X88     X88      |")
        print("|    \"Y88888 \"Y88888 \"Y8888  88888P' 88888P'      |")
        print("|        888                                      |")
        print("|   Y8b d88P                                      |")
        print("|    \"Y88P\"                                       |")
        print("|         Welcome to my Guessing Game!            |")
        print("|              Top Score: " + str(top_score) + "                       |")
        print("---------------------------------------------------")

        print("I have randomly picked a number between 1 and 100.")
        print("You need to try and guess it. I'll say higher or lower till you get it.")

        try:
            guess = int(input("What is your first number?\n"))
        except ValueError:
            print("You failed already... Lets start again but numbers only please!")
            start_game()

        # Start guessing
        while number != guess:
            try:
                if guess > 100 or guess < 1:
                    attempts += 1
                    print("You are already bad at this game...")
                    guess = int(input("The number is between and including 1 to 100! Try again...\n"))
                elif number > guess:
                    guess = int(input("Try higher! \n"))
                    attempts += 1
                elif number < guess:
                    guess = int(input("Try lower! \n"))
                    attempts += 1
                else:
                    print("There was an unforeseen error!!!")
            except ValueError:
                print("Use numbers only!\n")

        # The ending
        attempts += 1
        print("You got it right. Well Done!")
        print("It has only taken you " + str(attempts) + " guesses.")
        attempts = int(attempts)
        top_score = int(top_score)
        if top_score == 0:
            top_score = attempts
        elif top_score > attempts:
            top_score = attempts
        start_again = input("Would you like to start again? [Y]es or [N]o?")
        if start_again.lower() == "n":
            print("Thanks for playing!")
            break


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
