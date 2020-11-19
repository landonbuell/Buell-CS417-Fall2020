'''
Lexical Analysis.
Given an expression (a string), break it up into tokens,
and identify the type of each token.
'''

from typing import List, Tuple

def tokenize(expression: str, specials: str, whitespace: str) -> List[str]:
    '''
    Given an expression (a string), break it up into tokens.
    Inputs:
        expression: a string
        specials:   single-character tokens (usually operators)
        whitespace: characters that separate tokens (usually space)
    Return: a list of strings (each is a token)
    '''

    '''
    Method: implement a state machine, with three states:
    - OPERAND
    - SPECIAL
    - WHITESPACE
    Each character in the expression causes a transition among
    these three states.
    '''
    # The states
    IDLE       = 0
    OPERAND    = IDLE    + 1
    WHITESPACE = OPERAND + 1

    # Intial state
    state = IDLE

    # The list of tokens
    tokens = []
    for c in expression:
        if state == IDLE:

            # Here, I handle some transitions for you.
            # Notice that, in each case, I take some action,
            # and (optionally) change the state

            if c in whitespace:
                state = WHITESPACE
                continue
            elif c in specials:
                state = IDLE
                tokens.append(c)
            else: # It's an operand character.  Start an operand
                state = OPERAND
                operand = c

        # Task 1:
        # Now, you must handle the remaining cases
        # When you are done, remove most of the 'pass' statements.
        elif state == OPERAND:
            if c in whitespace:
                # save the operand
                pass
            elif c in specials:
                # save the operand, save the special
                pass
            else:
                # extend the operand
                pass

        elif state == WHITESPACE:
            if c in whitespace:
                # do nothing
                pass
            elif c in specials:
                # save the special
                pass
            else:
                # start an operand
                pass

    # Task 2: Check if we need to save the last operand

    return tokens

def lexer(tokens: List[str]) -> List[Tuple[str,str]]:
    '''
    Identify the type of every token:
      - number
      - variable
      - operator
      - unknown

    Input:  a list of tokens
    Return: a list of (type, token) pairs
    '''
    lexemes = []
    operators = "+-*/=()"
    for token in tokens:
        lex_type = 'unknown'
        lex_value = token

        # Task 3 and 4: What type is the token?




        # Leave this line here, at the end of the for-loop
        lexemes.append( (lex_value, lex_type) )
    return lexemes


def analyze_expression(expr: str) -> List[Tuple[str,str]]:
    '''
    Given an expression, tokenize it and do lexical analysis
    Input:  expression, a string
    Output: print the type and value of each token
    '''
    if type(expr) == str:
        tokens = tokenize(expr, "+-*/=()", " ")
    else:
        tokens = expr
    lexemes = lexer(tokens)
    for token, kind in lexemes:
        print ('  {:>6} : {:>6}'.format(token, kind))

def main():
    expr = "hello, how are,you?"
    print ('Tokenize "'+expr+'"', ":\n  ", tokenize(expr, "", " ,\t"))

    expr = "cost= total + (7.0 / 100)* total"
    print ('Tokenize "'+expr+'"', ":\n  ", tokenize(expr, "+-*/=()", " "))

    print()
    print("Analyze ['cost','=','total','+','(','7.0','/','100',')','*','total']:")
    analyze_expression(['cost', '=', 'total', '+', '(', '7.0',
                        '/', '100', ')', '*', 'total'])

if __name__ == "__main__":
    main()

