from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def check_answer(user_guess, number_to_guess, guess_count):
    if user_guess > number_to_guess:
        print("Too high.")
        return guess_count - 1
    elif user_guess < number_to_guess:
        print("Too low.")
        return guess_count - 1
    else:
        print(f"You got it! The answer was {number_to_guess}.")

def game():


    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = randint(1, 100)

    guess_count = set_difficulty()
    user_guess = 0

    while number_to_guess != user_guess:
        print(f"You have {guess_count} attempts remaining to guess the number")
        user_guess = int(input("Make a guess: "))

        guess_count = check_answer(user_guess, number_to_guess, guess_count)
        if guess_count == 0:
            game_running = False
            print(f"You've run out of guesses, you lose.")
        elif user_guess != number_to_guess:
            print("Guess again.")

game()