from typing import Dict

class Expression_Node(object): 
    """ Expression_Node is parent class for all Tree Nodes """
    
    def __str__(self):
        return 'an Expression_Node'

    def __repr__(self):
        """ Return Programmer reprsentation of instance """
        return "Expression Node: " + self._data + "\t"

    def get_value(self, symbol_table: Dict[str,float]) -> float:
        raise Exception("Should not evaluate this parent class")

    def is_leaf(self) -> bool:
        # Should return True/False if the node hasn't/has children
        # Useful when printing the tree.
        raise Exception("Should not evaluate this parent class")


class Operator_Node (Expression_Node):
    """ Operator_Node Hold Operator """

    def __init__(self,value,left=None,right=None):
        """ Constructor for Operand_Node Class """
        self._data = value
        self._left = left
        self._right = right

    def __str__(self):
        """ Return string representation of this node """
        return str(self._data)

    def __repr__(self):
        """ Return Programmer reprsentation of instance """
        return "Operator Node: " + self._data + "\t"

    def get_value(self, symbol_table):
        """ Return string representation of this node """
        if self._data == "+":
            return self._left.get_value(symbol_table) + \
                self._right.get_value(symbol_table)
        elif self._data == "-":
            return self._left.get_value(symbol_table) - \
                self._right.get_value(symbol_table)
        elif self._data == "*":
            return self._left.get_value(symbol_table) * \
                self._right.get_value(symbol_table)
        elif self._data == "/":
            return self._left.get_value(symbol_table) / \
                self._right.get_value(symbol_table)
        elif self._data == "=":
            tableUpdate = {self._left._data:self._right.get_value(symbol_table)}
            symbol_table.update(tableUpdate)
            return self._right
        else:
            raise NotImplementedError("Unknown Operator Type!")

    def is_leaf (self):
        """ Return T/F is node is a leaf """
        return False

class Operand_Node (Expression_Node):
    """ Operand_Node Holds Variable or Number """
    
    def __init__(self,value):
        """ Constructor for Expression_Node Class """
        self._data = value
        self._left = None
        self._right = None

    def __repr__(self):
        """ Return Programmer reprsentation of instance """
        return "Operand Node: " + self._data + "\t"

    def is_leaf (self):
        """ Return T/F is node is a leaf """
        if (self._left is None) and (self._right is None):
            return True
        else:
            return False
            
class Variable_Node (Operand_Node):
    """ Variable_Node Holds a string varibale pointer """
    
    def __init__(self,value):
        """ Constructor for Variable_Node Class """
        super().__init__(value)

    def __str__(self):
        """ Return string representation of this node """
        return str(self._data)

    def __repr__(self):
        """ Return Programmer reprsentation of instance """
        return "Variable Node: " + self._data + "\t"

    def get_value(self, symbol_table):
        """ Evalue this Node """
        token = self._data
        try:
            return symbol_table[token]  # adapted from parser417.py
        except KeyError as e:
            raise KeyError('Variable ' + token + ' is undefined')


class Number_Node (Operand_Node):
    """ Number_Node holds a literal numerical value """

    def __init__(self,value):
        """ Constructor for Number_Node Class """
        super().__init__(value)

    def __str__(self):
        """ Return string representation of this node """
        return str(self._data)

    def __repr__(self):
        """ Return Programmer reprsentation of instance """
        return "Number Node: " + str(self._data) + "\t"

    def get_value(self, symbol_table):
        """ Evalue this Node """
        return self._data