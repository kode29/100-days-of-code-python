from game_data import data
import random
from art import vs, logo

game_is_running = True
score = 0

def display_data(data):
    """Parse the incoming data into a formalized string"""
    return f"{data['name']}, a {data['description']}, from {data['country']}"

def check_answer(guess, a_follower_count, b_follower_count):
    """Check if the user guessed correctly"""
    if a_follower_count > b_follower_count:
        return guess=="a"
    else:
        return guess=="b"

compare_b = random.choice(data)
while game_is_running:
    print(logo)
    # This will pick up the previous value (B will also be A no matter the higher value)
    compare_a = compare_b

    compare_b = random.choice(data)
    # If, on the random chance, that random=random, re-do it
    if compare_b == compare_a:
        compare_b = random.choice(data)

    print(f"Compare A: {display_data(compare_a)}")
    print(vs)
    print(f"Against B: {display_data(compare_b)}")

    choice = input("Who has more followers (on Instagram)? Type 'A' or 'B': ").lower()

    # Clear the screen
    print("\n" * 20)
    print(logo)

    a_followers = int(compare_a['follower_count'])
    b_followers = int(compare_b['follower_count'])

    is_correct = check_answer(choice, a_followers, b_followers)

    if is_correct:
        score += 1
        print(f"You're right!: Current Score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_is_running = False