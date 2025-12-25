# BasicCalculator
# Week 3: Functions & Calculator
A simple CLI calculator to practice using DRY coding principles, multiple code files, and function handling.
The user enters a number, an operator, and another number, the program will procude the result. The user can then continue with further calculations, clear the current result, or close the calculator, or view the history log.

## Project Requirements

- One function per operation
- User selectes operation
- Minimize code duplication

## Secondary features

- Clear function
- Operation history
- Multi-step calculations

## Usage Instructions

- Must have Python3 installed
- Clone this repository
- run: python main.py

## What I learned

- Safely using user input to call functions
- Using multiple return values
- Managing multiple code files
- Avoiding recursive imports
- State management

## Example Usage

```
Welcome to my basic Calculator.
Please enter a number: 5
Please enter a operator: + 
Please enter a number: 2
5.0 + 2.0 = 7.0
Please enter a operator: *
Please enter a number: 6
7.0 * 6.0 = 42.0
Please enter a operator: / 
Please enter a number: 4
42.0 / 4.0 = 10.5
Please enter a operator: l
5.0 + 2.0 = 7.0
7.0 * 6.0 = 42.0
42.0 / 4.0 = 10.5
Please enter a operator: q
Thanks for using my calculator!
```

## Future Improvements
- Higher math functions, such as exponents and square roots
- Help System
- Memory function