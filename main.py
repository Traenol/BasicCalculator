from input import get_input
from constants import OPERATORS

def main():
    print("Welcome to my basic Calculator")
    running = True

    # The calculator result
    result = None
    # Start the app loop
    number1 = get_input(float)
    while running:
        operation, name = get_input("function", "Please select an operation. (+, -, *, /)")
        if operation == "q":
            break
        number2 = get_input(float)
        if number2 == "q":
            break
        if name == "divided by":
            result = operation(number1, number2, get_input)
        else:
            result = operation(number1, number2)
        print(f"{number1} {name} {number2} is {result}")
        number1 = result
    print("Thanks for using my calculator!")

# Start the calculator
main()