def add_numbers(first_operand, second_operand):
    return first_operand + second_operand

def subtract_numbers(first_operand, second_operand):
    return first_operand - second_operand

def multiply_numbers(first_operand, second_operand):
    return first_operand * second_operand

def divide_numbers(first_operand, second_operand, get_input_func):
    while second_operand == 0:
       second_operand = get_input_func(float, "Cannot divide by zero outside of a black hole. Try another number.\n")
    return first_operand / second_operand