from constants import OPERATORS

def get_input(return_class, prompt="Please enter a number.\n"):
    user_input = ""
    running = True
    while running:
        user_input = input(prompt)
        num = True
        items = user_input.split(".")
        for item in items:
            if not item.isdigit():
                num = False
        if num:
            user_input = return_class(user_input)
            running = False
    return user_input