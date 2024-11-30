from menu_data import MENU, resources

machine_is_on = True

money = float(0)

def check_resources(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def use_resources(drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]

def print_report():
    global money
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    formatted_money = "{:,.2f}".format(money)
    print(f"Money: ${formatted_money}")

def process_coins():
    """Returns the total calculated from coins inserted"""
    total = float(input("How many quarters?: ")) * .25
    total += float(input("How many dimes?: ")) * .10
    total += float(input("How many nickels?: ")) * .05
    total += float(input("How many pennies?: ")) * .01
    return total

def transaction_successful(cash_received, drink_cost):
    global money
    if cash_received >= drink_cost:
        money += drink_cost
        change = cash_received - drink_cost
        if change > 0:
            change = "{:,.2f}".format(change)
            print(f"Here is your ${change} in change")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded")
        return False


while machine_is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice in ("espresso", "latte", "cappuccino"):
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            # We're good. Ask for money
            total_cash_received = process_coins()
            if transaction_successful(total_cash_received, drink["cost"]):
                # We're good. Process the drink
                use_resources(drink["ingredients"])
                print(f"Here's your {choice} ☕. Enjoy!")
    elif choice == "report":
        print_report()
    elif choice == "off":
        print("Machine off")
        machine_is_on = False
    else:
        print("Invalid entry. Try again")