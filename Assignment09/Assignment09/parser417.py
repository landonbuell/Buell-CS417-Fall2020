import string
from typing import List, Dict, Any, Tuple

from stack import Stack

def prec(op: str) -> int:
    """Return the precedence of an operator.

    Parameter:
    ----------
    op : str
       an operator
    """
    if op in '*/':
        return 3
    elif op in '+-':
        return 1
    else:  # (, ), = have lowest priority
        return 0

def tokenize(line: str, specials: str, whitespace: str) -> List[str]:
    """Break a string into tokens.

    Parameters:
    -----------
    line : str
        an arithmetic expression
    specials: str
        single-character tokens
    whitespace: str
        separates ordinary tokens
    """
    tokens = []
    current_token = ''
    non_operands = specials + whitespace
    for i, c in enumerate(line):
        if c in non_operands:
            if current_token != '':
                tokens.append(current_token)
                current_token = ''
            if c in specials:
                tokens.append(c)
        else:
            current_token += c
    if current_token != '':
        tokens.append(current_token)
    return tokens

def is_operator(token: str) -> bool:
    """Determines whether a token is/isn't an operator

    Parameter:
    ----------
    token : str
        the token we need to classify
    """
    if type(token) == str:
        return token in '+-*/=()'
    else:
        return False

def is_variable_name(token: str) -> bool:
    """Determines whether a token is/isn't the name of a variable.

    Parameter
    ---------
    token : str
        the token we need to classify
    """
    if type(token) == float:
        return False

    if token[0] not in (string.ascii_letters + '_'):
        # First char must be letter or underscore
        return False
    else:
        # remaining chars must be letter, number, or underscore
        for c in token[1:]:
            if c not in (string.ascii_letters + '_' + string.digits):
                return False
        return True

def get_value(token: Any, symbol_table: Dict[str,float]) -> float:
    """Looks up the numerical value of a token, if it's not already a number.

    Parameters
    ----------
    token : Any type
        the token we want to evaluate
    symbol_table : dict(any -> float)
        stores values of all known variables
    """
    if type(token) == float:
        return token

    elif is_variable_name(token):
        try:
            return symbol_table[token]
        except KeyError as e:
            raise KeyError('Variable ' + token + ' is undefined')

def lexer(tokens: List[str]) -> List[Tuple[Any,str]]:
    """Classifies a list of tokens into operator/number/variable/unknown.

    Parameter
    ---------
    tokens : list of str
        the tokens we need to classify

    Returns
    -------
    list of (Any, str) tuples
        the classified tokens.  In each tuple, the token is first, and its
        lexical type is second.
    """
    lexemes = []
    for token in tokens:
        if is_operator(token):
            lexemes.append((token, 'operator'))
        else:
            try:
                value = float(token)
                lexemes.append((value, 'number'))
            except ValueError:
                if is_variable_name(token):
                    lexemes.append( (token, 'variable') )
                else:
                    lexemes.append( (token, 'unknown') )
    return lexemes

def to_postfix(infix_lexemes: List[Tuple[Any,str]]) -> List[Tuple[Any,str]]:
    """Convert an infix list into a postfix list.

    Parameters
    ----------
    infix_lexemes : list of (Any, str) tuples
        the lexemes, in infix order

    Returns
    -------
    list of (Any, str) tuples
        the same lexemes, in postfix order
    """
    pending_operators = Stack()
    postfix_expression = []
    for pair in infix_lexemes:
        (token, lex_type) = pair

        if lex_type == 'operator':
            if token == '(':
                pending_operators.push(pair)

            elif token == ')':
                while (not pending_operators.empty() and
                      pending_operators.top()[0] != '('):
                    postfix_expression.append(pending_operators.pop())

                if pending_operators.empty():
                    raise SyntaxError("Too many close parentheses")

                pending_operators.pop()

            else:
                while (not pending_operators.empty() and
                       prec(pending_operators.top()[0]) >= prec(token) and
                       pending_operators.top()[0] != '='):
                    postfix_expression.append(pending_operators.pop())
                pending_operators.push(pair)

        elif lex_type == 'number':
            postfix_expression.append(pair)

        elif lex_type == 'variable':
            postfix_expression.append(pair)

        else:
            raise SyntaxError('Bad token: "' + token + '"')

    while not pending_operators.empty():
        if pending_operators.top() == '(':
            raise SyntaxError("Too many open parentheses")
        postfix_expression.append(pending_operators.pop())

    return postfix_expression

def eval_postfix(postfix_expression: List[Tuple[Any,str]],
                 symbol_table: Dict[str,float]) -> float:
    """Evaluates a postfix expression.

    Parameters
    ----------
    postfix_expression: list of (Any, str) tuples
        the lexemes, in postfix order
    symbol_table : dict(any -> float)
        stores values of all known variables
        SIDE EFFECT: this may get changed if there is a = operator.

    Returns
    -------
    float
       the value of the expression
    """
    s = Stack()
    for token, lex_type in postfix_expression:
        if lex_type == 'operator':
            try:
                right = s.pop()
                left  = s.pop()
            except IndexError as e:
                raise SyntaxError('Too many operators')

            if token != '=':
                left = get_value(left, symbol_table)

            right = get_value(right, symbol_table)

            if token == '+':
                value = left + right
            elif token == '-':
                value = left - right
            elif token == '*':
                value = left * right
            elif token == '/':
                if right == 0:
                    raise ValueError('Division by zero')
                value = left / right
            elif token == '=':
                symbol_table[left] = right
                value = right
            else:
                raise ValueError('Bad operator: "' + token + '"')

            s.push(value)

        elif lex_type == 'variable':
            s.push(token)

        elif lex_type == 'number':
            value = float(token)
            s.push(value)

        else:
            raise SyntaxError('bad token: "' + token + '"')

    if len(s) > 1:
        raise SyntaxError('Too few operators')
    elif len(s) == 1:
        return get_value(s.pop(), symbol_table)
    else:
        return None

def main():
    """Let the user test all the above functions.
    Basically a simple calculator"""
    symbol_table = dict()
    while True:
        try:
            line = input('>> ')
        except EOFError:
            print( )
            break

        try:
            tokens = tokenize(line, '+-*/()=', ' ')
            lexemes = lexer(tokens)
            postfix_lexemes = to_postfix(lexemes)

            print('postfix:', postfix_lexemes)
            value = eval_postfix(postfix_lexemes, symbol_table)
            if value is not None:
                print( value )
        except SyntaxError as e:
            print( e )
        except KeyError as e:
            print( e )
        except ValueError as e:
            print( e )

if __name__ == '__main__':
    main()
