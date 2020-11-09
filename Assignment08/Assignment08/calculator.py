from stack import *
from typing import List, Dict, Any

def tokenize(line: str, specials: str, whitespace: str) -> List[str]:
    '''
    Given an expression, breaks it up into tokens

    Parameters:
    line:        a string
    specials:    single-character tokens (usually '+-*/=()')
    whitespace : characters that should be ignored (usually ' \t')

    Returns:
    a list of strings.  Each string is a token.
    '''
    return []

def precedence(operator: str) -> int:
    '''
    Precedence of operators.

    * / : highest
    + - : middle
    = () : lowest

    Parameter:
    operator: a single character

    Returns:
    1, 2, or 3 (low, middle, high precedence)
    '''
    return 0

def to_postfix(infix_expression: int) -> List[str]:
    '''
    Convert an infix expression into a postfix expression

    Parameter:
    infix_expression, a string

    Returns:
    a list of strings (the tokens in postfix form)
    '''

    # First, call tokenize to get the tokens from the infix expression.
    # Then, create a postfix list, a stack, and run the algorithm.
    return []

def eval_postfix(postfix_expression: List[Any], symbol_table: Dict[str,float]) \
    -> float:
    '''
    Evaluate a postfix expression.

    May modify the symbol table (if the expression contains an = operator).

    Parameters:
    postfix_expression, a list of tokens (may be strings or numbers)
    symbol_table: a dictionary with the currently-known variables

    Returns:
    the value of the expression.
    '''
    return 0

def main():
    symbol_table = dict()
    while True:
        try:
            expression = input('>>> ')
        except EOFError:
            print()
            break

        if expression[0] == '#':
            # Comment line.  Print it, and ignore it.
            print(expression)
            continue

        postfix = to_postfix(expression)
        value = eval_postfix(postfix, symbol_table)
        print (value)

if __name__ == '__main__':
    main()


