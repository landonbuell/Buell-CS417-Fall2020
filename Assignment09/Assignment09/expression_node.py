from typing import Dict

class Expression_Node(object):
    def __str__(self):
        return 'an Expression_Node'

    def get_value(self, symbol_table: Dict[str,float]) -> float:
        raise Exception("Should not evaluate this parent class")

    def is_leaf(self) -> bool:
        # Should return True/False if the node hasn't/has children
        # Useful when printing the tree.
        raise Exception("Should not evaluate this parent class")



