import art
print(art.logo)

print(f"Welcome to the secret auction program.")

auction_running = True
bids_placed = {}

while auction_running:
# TODO-1: Ask the user for input
    name = input("What is your name?: ")
    bid = input("What is your bid? $")

# TODO-2: Save data into dictionary {name: price}
    bids_placed[name] = bid

# TODO-3: Whether if new bids_placed need to be added
    repeat = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if repeat == "no":
        auction_running = False

    print("\n" * 20)

# TODO-4: Compare bids_placed in dictionary
winner_bid = 0
winner_name = ""

for key in bids_placed:
    if int(bids_placed[key]) > int(winner_bid):
        winner_name = key
        winner_bid = bids_placed[key]

print(f"The winner is {winner_name} with a bid of ${winner_bid}")