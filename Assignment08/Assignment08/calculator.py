from stack import *
from typing import List, Dict, Any
import string

def tokenize(line: str, specials: str, whitespace: str) -> List[str]:
    '''
    Given an expression, breaks it up into tokens

    Parameters:
    line:        a string
    specials:    single-character tokens (usually '+-*/=()')
    whitespace : characters that should be ignored (usually ' \t')

    Returns:
    a list of strings.  Each string is a token. Adpated from Lab 16
    '''
    IDLE,OPERAND,WHITESPACE = 0,1,2
    tokens = []
    state = IDLE
    for c in line:           # each character:
        if state == IDLE:
            if c in whitespace:
                state = WHITESPACE
                continue
            elif c in specials:
                state = IDLE
                tokens.append(c)
            else: # It's an operand character.  Start an operand
                state = OPERAND
                operand = c
        elif state == OPERAND:
            if c in whitespace:
                # end & save the operand
                tokens.append(operand)
                state = WHITESPACE
            elif c in specials:
                # save the operand, save the special
                tokens.append(operand)      # store op. in tokens
                tokens.append(c)            # store c in tokens
                state = IDLE
            else:
                # extend the operand
                operand += c
                state = OPERAND
        elif state == WHITESPACE:
            if c in whitespace:
                # do nothing
                pass
            elif c in specials:
                # save the special
                tokens.append(c)
                state = IDLE
            else:
                # start an operand
                operand = c
                state = OPERAND
    if state == OPERAND:
        tokens.append(operand)
    return tokens

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
    if operator in "*/":
        return 3
    elif operator in "+-":
        return 2
    elif operator in "=()":
        return 1
    else:
        raise ValueError()

def IsOperand(token):
    """
    Determine if token is operand: T/F
    """
    if token in "+-*/=":    # operator
        return False        # not operand
    else:                   # otherwisr
        try:                        # attempt
            token = float(token)    # make float?
            # No except? It's a number
            return True
        except ValueError:
            # test if Valid Python name
            if ValidPythonName(token) == True:  # is valid
                return True
            else:
                raise ValueError()
            
def ValidPythonName(token):
    """ Test if token is a valid Python name """
    if (token[0] not in "_" + string.ascii_letters):
        return False        # must be "_" or a letter
    for char in token[1:]:  # other token characters
        if (char not in "_" + string.ascii_letters + string.digits):
            return False    # not a valid name
    return True             # is a valid name


def to_postfix(infix_expression: int) -> List[str]:
    '''
    Convert an infix expression into a postfix expression

    Parameter:
    infix_expression, a string

    Returns:
    a list of strings (the tokens in postfix form)
    '''

    # First, call tokenize to get the tokens from the infix expression.
    tokensList = tokenize(infix_expression,specials='+-*/=()',whitespace=' \t')

    # Then, create a postfix list, a stack, and run the algorithm.
    operatorStack = Stack()         # stack that hold operators
    postfix = []                    # list to hold postfix expression
    for token in tokensList:        # each token in the list
        if token == "(":
            operatorStack.push(token)   # add
        elif IsOperand(token) == True:  # not an operator (is operand)
            postfix.append(token)       # add to token
        elif token == ")":         
            while (operatorStack.empty() == False) and (operatorStack.top() != "(" ):
                value = operatorStack.pop() # pop from top
                postfix.append(value)       # add to postfix expression
            operatorStack.pop()             # pop the open pareth.
        else:                               # token is operator
            precCur = precedence(token)     # get precedence of current op
            try:
                precTop = precedence(operatorStack.top())
            except:
                precTop = 0
            while (operatorStack.empty() == False) and (precTop >= precCur):
                value = operatorStack.pop()                 # pop op.
                postfix.append(value)                       # add to postfix
                precTop = precedence(operatorStack.top())   # re-eval top prec
            operatorStack.push(token)
    # Done w/ line, clena up stack
    while not operatorStack.empty():    # stack not empty:
        value = operatorStack.pop()     # pop
        postfix.append(value)           # add to postfix
    return postfix

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
    postfixStack = Stack()              # postfix stack
    for token in postfix_expression:    # each token
        if IsOperand(token):            # is an operand
            postfixStack.push(token)    # push to stack
        else:                           # it's an operator
            rightOperand = postfixStack.pop()
            leftOperand = postfixStack.pop()
            operatorList = [leftOperand,rightOperand]

            for i in range(len(operatorList)):  # each operand
                try:                        # attempt
                    operatorList[i] = float(operatorList[i])            # convert to float
                except:                                                 # cannot be float, is variable
                    if operatorList[i] in symbol_table:                 # already in symbol table
                        operatorList[i] = symbol_table[operatorList[i]] # get float val of op
            leftOperand,rightOperand = operatorList[0],operatorList[1]

            if token == "+":
                result = leftOperand + rightOperand
            elif token == "-":
                result = leftOperand - rightOperand
            elif token == "*":
                result = leftOperand * rightOperand
            elif token == "/":
                result = leftOperand / rightOperand
            elif token == "=":
                symbol_table.update({leftOperand:rightOperand})
                result = rightOperand
            else:
                raise ValueError()
            postfixStack.push(result)
    return postfixStack.top()


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


