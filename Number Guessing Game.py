import random

# Number Guessing Game

while True:
    number = random.randint(1, 100)
    attempts = 7
    guessed = False

    print("\nGuess the number between 1 and 100")

    while attempts > 0:
        try:
            guess = int(input("Enter guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts -= 1

        if guess == number:
            print("Correct! You guessed it.")
            guessed = True
            break
        elif guess > number:
            print("Too high!")
        else:
            print("Too low!")

        print("Attempts left:", attempts)

    if not guessed:
        print("You failed. Number was:", number)

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break