import art

def add(n1, n2):
    """Add 2 numbers together (a+b)"""
    return n1 + n2
def subtract(n1, n2):
    """Subtract 2 numbers together (a-b)"""
    return n1 - n2
def multiply(n1, n2):
    """Multiply 2 numbers together (a*b)"""
    return n1 * n2
def divide(n1, n2):
    """Divide 2 numbers together (a/b)"""
    return n1 / n2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    """Basic Calculator - 2 inputs (number1, number2)"""
    print(art.logo)
    is_running = True
    num1 = float(input("What's the first number?: "))

    while is_running:
        for symbol in operators:
            print(symbol)
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        result = float(operators[operation](num1, num2))
        print(f"{num1} {operation} {num2} = {result}")

        repeat = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

        if repeat == "y":
            num1 = result
        else:
            is_running = False
            print("\n"*20)
            calculator()

calculator()