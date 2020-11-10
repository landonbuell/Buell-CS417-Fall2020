"""
Landon Buell
Alejo Hausner
CS 417.01
10 Nov 2020
"""

import console # Need this for testing, please don't remove this line
from stack import Stack

# Task 1: import the Stack class from the stack module

def is_operator(token):
    # Task 2: Identify operators
    validOperators = "+-*/="
    if token in validOperators:
        return True
    else:
        return False

def eval_postfix(expression):
    s = Stack()
    for token in expression:
        if is_operator(token):

            # Task 3: handle an operator (and Task 7 is here too):
            # - pop into right_operand

            # - pop into left_operand
            if s.empty():
                return "Too Many Operators"
            else:
                operandRight = s.pop()
            if s.empty():
                return "Too Many Operators"
            else:
                operandLeft = s.pop()

            # - add, subtract, multiply, or divide those two values, into result
            if token == "+":
                result = operandLeft + operandRight
            elif token == "-":
                result = operandLeft - operandRight
            elif token == "*":
                result = operandLeft * operandRight
            elif token == "/":
                result = operandLeft / operandRight
            else:
                raise NotImplementedError()
            # - push result
            s.push(result)

        else:

            # Task 4: handle an operand: (and Task 6 is here too)
            try:        # convert to float
                token = float(token)
            except:
                raise NotImplementedError()
            # - push it
            s.push(token)

    # Task 5: get the expression's value (and Task 8 is here too).
    # After all tokens have been processed, the expresion's value
    # will be at the top of the stack.
    # - pop into result
    if len(s) > 1:
        return "Too Many Operands"
    
    value = s.pop()
    # - return result
    return value

def main():
    while True:
        try:
            line = input("> ")
        except EOFError:
            break

        if line.startswith("#"):
            print()
            print(line)
            continue

        tokens = line.rstrip('\n\r').split()
        result = eval_postfix(tokens)
        print (result)

if __name__ == '__main__':
    main()

