import sys
from random import randint


if __name__ == "__main__":
    count = 0
    rand = randint(1, 99)
    print(rand)
    print("This is an interactive guessing game!\
\nYou have to enter a number between 1 and 99 to find out the secret number.\
\nType 'exit' to end the game.\
\nGood luck!\
\n")
    while (True):
        guess = input("What's your guess between 1 and 99?\
\n>> ")
        if (guess == 'exit'):
            print("Goodbye!")
            exit()
        if (not guess.isnumeric()):
            print("That's not a number.")
        else:
            if (int(guess) == rand and not count):
                print("Congratulations! You got it on your first try!")
                exit()
            elif (int(guess) == rand):
                print(f"Congratulations, you've got it!\n\
You won in {count + 1} attempts!")
                exit()
            elif (int(guess) > rand):
                print("Too high!")
            else:
                print("Too low!")
            count += 1
