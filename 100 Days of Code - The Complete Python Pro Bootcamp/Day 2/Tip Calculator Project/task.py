print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total = round((bill * (1+(tip/100))/people), 2)
total = "{:.2f}".format(total) # Add 2 decimals if 0
print(f"You owe $ {total}")