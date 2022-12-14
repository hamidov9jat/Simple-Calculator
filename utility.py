import os
from art import logo


def clear_console():
    os.system('cls')


def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def subtract(n1, n2):
    return n1 - n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    while True:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        # Return the identifier for appropriate function
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        chosen = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.\n"
                       f"Type anything else to exit:\n")

        if chosen == 'y':
            num1 = answer
            continue
        elif chosen == 'n':
            clear_console()
            # To indicate that it should be started again
            return True

        return False
