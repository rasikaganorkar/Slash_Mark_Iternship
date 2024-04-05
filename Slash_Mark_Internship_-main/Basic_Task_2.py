import random
import time

custom_number = random.randint(1, 300)

def intro():
    print("Hello there! What's your name?")
    name = input()
    print(f"Nice to meet you, {name}! We're about to play a game. I'm thinking of a number between 1 and 300.")
    time.sleep(0.5)
    print("Take a guess!")
    return name  # Return the name entered by the user

def make_guess(name):  # Accept the name as an argument
    attempts_taken = 0
    while attempts_taken < 7:
        time.sleep(0.25)
        user_input = input("Your guess: ")
        try:
            guess = int(user_input)
            if 1 <= guess <= 300:
                attempts_taken += 1
                if attempts_taken < 7:
                    if guess < custom_number:
                        print("Your guess is too low!")
                    elif guess > custom_number:
                        print("Your guess is too high!")
                    if guess != custom_number:
                        time.sleep(0.5)
                        print("Try again!")
                if guess == custom_number:
                    break
            else:
                print("Please enter a number between 1 and 300.")
        except ValueError:
            print("Oops! That doesn't look like a number. Try again.")

    if guess == custom_number:
        attempts_taken = str(attempts_taken)
        print(f'Congratulations, {name}! You guessed my number in {attempts_taken} attempts!')
    else:
        print(f"Sorry, {name}. The number I was thinking of was {custom_number}.")

play_again = "yes"
while play_again.lower() in ("yes", "y"):
    player_name = intro()  # Get the name from the intro function
    make_guess(player_name)  # Pass the name to the make_guess function
    play_again = input("Do you want to play again? (yes/no): ")
