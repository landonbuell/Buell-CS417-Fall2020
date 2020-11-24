from typing import List, Dict, Tuple, Any

from stack import Stack
from parser417 import lexer, tokenize, eval_postfix, to_postfix
from expression_node import *

def to_tree(postfix_expression: List[Tuple[Any,str]]) -> Expression_Node:
    '''
    Convert an postfix (a list of lexemes)
    into a parse tree.
    '''

    # Your code goes here

    # Replace the following line:
    return Expression_Node()

def eval_tree(node: Expression_Node, symbol_table: Dict[str,float]) -> float:
    '''
    Evaluate a parse tree.
    Call the node's get_value() method;
    that's where all the work gets done,
    if you have a properly-built hierarchy of classes.
    '''

    return None

def print_tree(node: Expression_Node) -> None:
    '''
    Print the tree "sideways".
    Method: use inorder traversal.
    Details:
    You need to indent based on each node's depth. Hence,
    you have to pass the depth.  That's why you need to
    write a "helper" function (with two parameters, not one)
    that does actual the inorder traversal.
    '''

    print( 'print_tree not implemented' )

def main():
    symbol_table = dict()
    while True:
        try:
            line = input('>> ')
        except EOFError:
            print()
            break

        if line[0] == '#':
            # Comment line.  Print it, and ignore it.
            print(line)
            continue

        try:
            tokens = tokenize(line, '+-*/()=', ' ')
            lexemes = lexer(tokens)
            postfix = to_postfix(lexemes)
            root = to_tree(postfix)
            print_tree(root)
            value = eval_tree(root, symbol_table)
            if value is not None:
                print( value )
        except SyntaxError as e:
            print( e )
        # Here, add more 'except' clauses, to catch every possible
        # error that is raised by various parts of your code.
        # See also parser417 for errors raised there.

if __name__ == '__main__':
    main()

