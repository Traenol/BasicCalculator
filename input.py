from constants import OPERATORS
from operations import add_numbers, subtract_numbers, multiply_numbers, divide_numbers

def get_input(return_class, prompt="Please enter a number.\n"):
    user_input = ""
    running = True
    while running:
        user_input = input(prompt)
        if return_class == "function":
            if user_input in OPERATORS:
                match user_input:
                    case "+":
                        return add_numbers, "plus"
                    case "-":
                        return subtract_numbers, "minus"
                    case "*":
                        return multiply_numbers, "times"
                    case "/":
                        return divide_numbers, "divided by"
            else:
                prompt = "Please enter a valid option."
                continue
        else:
            num = True
            items = user_input.split(".")
            for item in items:
                if not item.isdigit():
                    num = False
            if num:
                user_input = return_class(user_input)
                running = False
    return user_input