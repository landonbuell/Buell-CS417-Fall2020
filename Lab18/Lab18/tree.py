class Node:
    def __init__(self, x = None, l = None, r = None):
        """Constructor the Node class."""
        self.data  = x
        self.left  = l
        self.right = r

    def is_leaf(self):
        return self.left == None and self.right == None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        result = '(' + repr(self.data) + ' @' + str(id(self)) +\
                 ' left -> '
        if self.left == None:
            result += 'None'
        else:
            result += '@' + str(id(self.left))
        result += ' right -> '
        if self.right == None:
            result += 'None'
        else:
            result += '@' + str(id(self.right))
        result += ')'
        return result

class Tree:
    def __init__(self, orig = None):
        """Constructor the Tree class.  Optionally, insert some values"""
        self.root = None
        if orig != None:
            for x in orig:
                self.insert(x)

#############################################################
#
# The following methods will call the methods that YOU must implement
#
#############################################################

    def __len__(self):
        return self.subtree_size(self.root)

    def height(self):
        return self.subtree_height(self.root)

    def sum(self):
        return self.subtree_sum(self.root)

    def __contains__(self, value):
        return self.subtree_contains(value, self.root)

    def deepest_value(self):
        if self.root == None:
            return [None, 0]
        else:
            return self.subtree_deepest( self.root, 1)

######################################################################
#
# YOU MUST MODIFY THE METHODS BELOW THIS LINE
# (But look at the methods in the section just above,
#  to see how recursion starts)
#
# | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
# v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v

    ''' Exercise 1: return True/False if self.root is/isn't None '''
    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    ''' Exercise 2: return 0 if node is None,
        otherwise 1 + left size + right size '''
    def subtree_size(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.subtree_size(node.left) + self.subtree_size(node.right)

    ''' Exercise 3: return 0 if node is None,
        otherwise 1 + max of left and right heights '''
    def subtree_height(self, node):
        if node is None:
            return 0
        else:
            return 1 + max([self.subtree_height(node.left),self.subtree_height(node.right)])

    ''' Exercise 4: start at root, and loop: node = node.right '''
    def rightmost_data(self):
        currentNode = self.root
        while currentNode.right is not None:
            currentNode = currentNode.right
        return currentNode

    ''' Exercise 5: return 0 if node is None,
        otherwise data + left sum + right sum '''
    def subtree_sum(self,node):
        if node is None:
            return 0
        else:
            return node.data + self.subtree_sum(node.left) + self.subtree_size(node.right)

    ''' Exercise 6: False if node is None,
        otherwise go right or left until you find value '''
    def subtree_contains(self, value, node):
        if node is None:
            return False
        elif node.data == value:
            return True 
        else:
            return self.subtree_contains(value,node.left) or self.subtree_contains(value,node.right)

    ''' Exercise 7: return node's data and depth, if it's a leaf,
        otherwise find deepest in both subtrees, return deeper pair '''
    def subtree_deepest(self, node, depth):
        return [None,0]


# ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
# | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
#
# THE METHODS YOU MUST MODIFY ARE ABOVE THIS LINE
#
#########################################################################

    def insert(self, value):
#        print 'insert: value=',value
#        print 'before add, tree is:',
#        print repr(self)

        if self.root == None:
            self.root = Node(value, None, None)
        else:
            p = self.root
            while True:
                if p.data == value:
                    return False
                elif value < p.data:
                    if p.left == None:
                        p.left = Node(value)
                        return True
                    else:
                        p = p.left
                else: # value > p.data
                    if p.right == None:
                        p.right = Node(value)
                        return True
                    else:
                        p = p.right

    def inorder(self):
        for x in self.inorder_helper(self.root):
            yield x

    def inorder_helper(self, node):
        if node != None:
            for x in self.inorder_helper(node.left):
                yield x
            yield node.data
            for x in self.inorder_helper(node.right):
                yield x

    def __str__(self):
        return str(x for x in self.inorder())

    def __repr__(self):
        result = self.subtree_str(self.root, 0) + '\n'
        result += 'Tree(\n'
        result += self.subtree_repr(self.root, 0)
        result += ')'
        return result

    def subtree_repr(self, node, depth):
        if node != None:
            r_repr = self.subtree_repr(node.right, depth+1)
            l_repr = self.subtree_repr(node.left,  depth+1)
            return r_repr + \
                   '    ' + '  ' * depth + repr(node) + '\n' +\
                   l_repr
        else:
            return ''

    def subtree_str(self, node, depth):
        if node != None:
            r_str = self.subtree_str(node.right, depth+1)
            l_str = self.subtree_str(node.left,  depth+1)
            return r_str + \
                   '    ' + '  ' * depth + str(node) + '\n' +\
                   l_str
        else:
            return ''

def main():
    empty_tree = Tree()

    print( 'Is it empty?', empty_tree.is_empty() )

    tree = Tree([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7])


    print( 'tree values:', [x for x in tree.inorder()] )
    print( 'repr(tree):' )
    print( repr(tree) )

    print( 'size         :',len(tree) )
    print( 'height       :',tree.height() )
    print( 'rightmost    :',tree.rightmost_data() )
    print( 'sum          :',tree.sum() )
    print( 'contains 5?  ', (5 in tree) )
    print( 'contains 0?  ', (0 in tree) )
    [value, depth] = tree.deepest_value()
    print( 'deepest value:',value,'at depth',depth )

if __name__ == '__main__':
    main()


