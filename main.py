from input import get_input
from constants import OPERATORS

def main():
    print("Welcome to my basic Calculator")
    running = True

    # The calculator result
    result = None
    # Start the app loop
    number1 = get_input(float)
    operation, name = get_input("function", "Please select an operation. (+, -, *, /)")
    number2 = get_input(float)
    print(f"{number1} {name} {number2} is {operation(number1, number2)}")

# Start the calculator
main()