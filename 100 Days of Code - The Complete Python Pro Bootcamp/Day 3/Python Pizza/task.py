print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

small_pizza_price = 15
medium_pizza_price = 20
large_pizza_price = 25

total = 0
if size == "S":
    total += small_pizza_price
elif size == "M":
    total += medium_pizza_price
elif size == "L":
    total += large_pizza_price

if pepperoni == "Y":
    if size == "S":
        total += 2
    else:
        total += 3

if extra_cheese == "Y":
    total += 1

print(f"Your final bill is: ${total}.")

