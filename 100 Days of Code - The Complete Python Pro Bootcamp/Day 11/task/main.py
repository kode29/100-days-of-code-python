import random
import art

def game():
    """The Game!"""
    print(art.logo)
    user_cards = []
    dealer_cards = []

    for _ in range(0,2):
        deal_card(user_cards)
        deal_card(dealer_cards)

    user_cards_sum = calculate_score(user_cards)
    dealer_cards_sum = calculate_score(dealer_cards)

    is_running = True
    while is_running:
        user_cards_sum = calculate_score(user_cards)
        dealer_cards_sum = calculate_score(dealer_cards)

        print(f"   Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
        print(f"   Computer's first card: {dealer_cards[0]}")

        if user_cards_sum==0 or dealer_cards_sum == 0 or user_cards_sum > 21:
            is_running = False
        else:
            hit_or_pass = input(f"Type 'y' to get another card, type 'n' to pass: ").lower()

            if hit_or_pass == "y":
                deal_card(user_cards)
            else:
                is_running = False

    while dealer_cards_sum<=17 and dealer_cards_sum!=0:
        print(f"Dealer Draws...")
        deal_card(dealer_cards)
        dealer_cards_sum = calculate_score(dealer_cards)

    print(f" Your final hand: {user_cards}, final score: {user_cards_sum}")
    print(f" Computer's final hand: {dealer_cards}, final score: {dealer_cards_sum}")
    print(compare(user_cards_sum, dealer_cards_sum))

def compare(user_cards_sum, dealer_cards_sum):
    """Compares the user score u_score against the computer score c_score."""
    if dealer_cards_sum == user_cards_sum:
        return "It's a Draw"
    elif dealer_cards_sum == 0:
        return "Dealer wins with Blackjack"
    elif user_cards_sum == 0:
        return "You win with Blackjack"
    elif dealer_cards_sum > 21:
        return "Dealer Busts. You Win!"
    elif user_cards_sum > 21:
        return "You went over. You lose"
    elif dealer_cards_sum > user_cards_sum:
        return "You lose"
    elif dealer_cards_sum < user_cards_sum:
        return "You Win!"

def calculate_score(cards):
    """Calculate the sum of the cards (Ace is 11 if < 21, or 1 if > 21)"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def deal_card(player):
    """Draw a card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player.append(random.choice(cards))

while input("Do you want to play a game of Blackjack? (y/n): ").lower() == "y":
    print("\n"*20)
    game()
