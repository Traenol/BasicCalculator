from constants import STATES
from handlers import operand_handler, operator_handler, calculate_handler

STATES_MATRIX = {
    STATES.EXPECTING_LEFT_OPERAND: (operand_handler, "Please enter a number: "),
    STATES.EXPECTING_OPERATOR: (operator_handler, "Please enter a operator: "),
    STATES.EXPECTING_RIGHT_OPERAND: (operand_handler, "Please enter a number: "),
    STATES.CALCULATE: (calculate_handler, "Calculating..."),
}

def main():
    print("Welcome to my basic Calculator.")
    # Starting state
    context = [] # [operand_1, operator, operand_2]
    history = [] # Array of strings, eg: ['5.0 + 2.0 = 7.0', '7.0 - 7.0 = 0.0']
    current_state = STATES.EXPECTING_LEFT_OPERAND
    # Start the main app loop
    while True:
        # Check if we need input or to calculate the current inputs
        if current_state is not STATES.CALCULATE:
            # Not ready, get input
            user_input = input(STATES_MATRIX[current_state][1])
        # Handle input
        current_state = STATES_MATRIX[current_state][0](user_input, context, history)

# Start the calculator
main()