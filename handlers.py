from constants import STATES, OPERATOR_FUNCTIONS
from input import validate_operand_input, validate_operator_input
import sys

def command_clear(context, history=None):
    context.clear()
    return STATES.EXPECTING_LEFT_OPERAND

def command_help(context, history=None):
    pass

def command_quit(context, history=None):
    print("Thanks for using my calculator!")
    sys.exit(0)

def command_log(context, history):
    for entry in history:
        print(entry)
    return

COMMANDS = {"c": command_clear, "h": command_help, "q": command_quit, "l": command_log}

def operand_handler(input, context, history=None):
    # Check for command input
    if input.lower() in COMMANDS:
        state = COMMANDS[input.lower()](context, history)
        return STATES.EXPECTING_LEFT_OPERAND if not state else state
    try:
        # See if we can cast to a float
        if validate_operand_input(input):
            state = None
            # store the input in the context
            if context:
                state = STATES.CALCULATE
            context.append(float(input))
            return STATES.EXPECTING_OPERATOR if not state else state
        # Not a valid number
        return  STATES.EXPECTING_LEFT_OPERAND
    except ValueError:
        # Return the current state
        return  STATES.EXPECTING_LEFT_OPERAND


def operator_handler(input, context, history=None):
    if input.lower() in COMMANDS:
        state = COMMANDS[input.lower()](context, history)
        return STATES.EXPECTING_RIGHT_OPERAND if not state else state
    try:
        if validate_operator_input(input):
            context.append(input)
            return STATES.EXPECTING_RIGHT_OPERAND
        return STATES.EXPECTING_OPERATOR
    except IndexError:
        return STATES.EXPECTING_OPERATOR
    
def calculate_handler(input, context, history):
    result = OPERATOR_FUNCTIONS[context[1]](context[0],context[2])
    if type(result) != float:
        print(result)
        command_clear(context)
        return STATES.EXPECTING_RIGHT_OPERAND
    else:
        result_string = f"{context[0]} {context[1]} {context[2]} = {result}"
        print(result_string)
        history.append(result_string)
        command_clear(context)
        context.append(result)
    return STATES.EXPECTING_OPERATOR
