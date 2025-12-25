from constants import OPERATOR_FUNCTIONS

def validate_operand_input(input):
    try:
        temp = float(input)
        return True
    except:
        return False

def validate_operator_input(input):
    try:
        operator_func = OPERATOR_FUNCTIONS[input]
        return True
    except:
        return False
