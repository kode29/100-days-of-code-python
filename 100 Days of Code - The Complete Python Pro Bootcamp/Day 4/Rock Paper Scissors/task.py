import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
game_text = ["Rock", "Paper", "Scissors"]

print("Welcome to Rock/Paper/Scissors.")

player_choice = int(input("Choose: Rock [1], Paper [2], or Scissors [3]: "))
print(game_images[player_choice-1])
if player_choice >= 0 and player_choice <= 3:
    print(f"Your choice: {game_text[player_choice-1]}")

computer_choice = random.randint(1,3)
print(game_images[computer_choice-1])
print(f"Computer chose: {game_text[computer_choice-1]}")

# Game logic
if player_choice > 3 or player_choice < 0:
    print("Invalid selection.")
elif computer_choice < player_choice or (computer_choice == 3 and player_choice == 1):
    print("You Win!")
elif computer_choice == player_choice:
    print("It's a TIE!")
else:
    print("You lose")