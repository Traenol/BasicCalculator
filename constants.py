from enum import Enum
from operations import add_numbers, subtract_numbers, multiply_numbers, divide_numbers

class STATES(Enum):
    EXPECTING_LEFT_OPERAND = 0
    EXPECTING_OPERATOR = 1
    EXPECTING_RIGHT_OPERAND = 2
    CALCULATE = 3

OPERATOR_FUNCTIONS = {
    "+": add_numbers,
    "-": subtract_numbers,
    "*": multiply_numbers,
    "/": divide_numbers
    }