'''
A Binary Search Tree (BST)
This BST implements a dictionary, so each node in the tree stores
a key and a value.

To insert into the tree, invoke the __setitem__ method, thus:
      tree[key] = value
   If the key is not in the tree, a new (key, value) node is inserted
   If the key IS in the tree, its value is changed.

'''


'''
A node in the BST.
It stores a key, a value, and two children pointers.
'''
class Node:
    def __init__(self, key = None, value = None, l = None, r = None):
        self.key   = key
        self.value = value
        self.left  = l
        self.right = r


    def child_count(self):
        count = 0
        if self.left is not None:
            count += 1
        if self.right is not None:
            count += 1
        return count

    def is_single_parent(self):
        return self.child_count() == 1

    def del_child(self, left_child):
        if left_child:
            self.left  = None
        else:
            self.right = None

    def get_single_child(self):
        if self.left is None:
            return self.right
        else:
            return self.left

    def swap_data(self, other):
        (self.key,   other.key)   = (other.key,   self.key)
        (self.value, other.value) = (other.value, self.value)

    def is_leaf(self):
        return self.left == None and self.right == None

    def __str__(self):
        return '(' + str(self.key) + ' : ' + str(self.value) + ')'

    def __repr__(self):
        result = '(' + repr(self.key) + ' : ' +\
                 repr(self.value) + ' @' + str(id(self)) +\
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


class BST:

    '''
    All the code below this line are methods of the BST class.
    '''

    '''
    Initializer.
    If the argument orig is None, build an empty tree.
    If it's a dict, insert all its key-value pairs
    '''
    def __init__(self, orig = None):
        self.root = None
        if orig is not None and type(orig) == dict:
            for x in orig:
                # Here we insert a key-value pair
                self[x] = orig[x]

    '''
    Iterate through the keys
    Use thus:
       for key in tree:
          ....
    '''
    def __iter__(self):
        for x in self.keys():
            yield x

    '''
    This does the work of __iter__
    Uses the helper method inorder_keys(node)
    '''
    def keys(self):
        for x in self.inorder_keys(self.root):
            yield x

    '''
    Similar to keys(), but iterates through the values instead
    Also uses a helper method.
    '''
    def values(self):
        for x in self.inorder_values(self.root):
            yield x

    '''
    Helper method for keys().
    Runs inorder traversal
    '''
    def inorder_keys(self, node):
        if node != None:
            for key in self.inorder_keys(node.left):
                yield key
            yield node.key
            for key in self.inorder_keys(node.right):
                yield key

    '''
    Helper method for keys().
    Also runs inorder traversal
    '''
    def inorder_values(self, node):
        if node != None:
            for value in self.inorder_values(node.left):
                yield value
            yield node.value
            for value in self.inorder_values(node.right):
                yield value

    '''
    Height of tree.
    Uses helper method height_of_subtree(node)
    '''
    def height(self):
        return self.height_of_subtree(self.root)

    '''
    Helper method for height
    '''
    def height_of_subtree(self, node):
        if node == None:
            return 0
        else:
            left_height  = self.height_of_subtree(node.left)
            right_height = self.height_of_subtree(node.right)
            return 1 + max(left_height, right_height)

    '''
    As its name suggests, finds the right-most node in the
    subtree whose root is passed in.
    '''
    def rightmost_node(self, node):
        if node == None:
            return None
        else:
            p = node
            while p.right != None:
                p = p.right
            return p

    '''
    Finds left-most node in the tree subtree
    whose root is passed in
    '''
    def leftmost_node(self, node):
        if node == None:
            return None
        else:
            p = node
            while p.left != None:
                p = p.left
            return p

    '''
    Adds up all the values in the tree
    '''
    def subtree_sum(self,node):
        if node == None:
            return 0
        else:
            return node.value +\
                self.subtree_sum(node.left) +\
                self.subtree_sum(node.right)

    '''
    Checks if tree contains the given key.
    Not recursive, just walks left or right until the
    key is found, or not found

    Use thus:
       if key in tree:
          ....

    '''
    def __contains__(self, key):
        node = self.root
        while node is not None:
            if node.key == key:
                return True
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return False

    '''
    Retrieves the value associated with the given key
    Very similar to __contains__

    Use thus:
       x = tree[key]
    '''
    def __getitem__(self, key):
        node = self.root
        while node is not None:
            if node.key == key:
                return node.value
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        raise KeyError

    '''
    Sets a value for the given key.
    If the key is in the tree, replaces its value
    If not, inserts a key-value pair.

    Use thus:
        tree[key] = value
    '''
    def __setitem__(self, key, value):
        if self.root is None:
            self.root = Node(key,value)
            return
        else:
            node = self.root
            while node is not None:
                if node.key == key:
                    node.value = value
                    return
                elif key < node.key:
                    if node.left is None:
                        node.left = Node(key, value)
                        return
                    else:
                        node = node.left
                else:
                    if node.right is None:
                        node.right = Node(key, value)
                        return
                    else:
                        node = node.right

    '''
    Delete a key from the tree, and its associated value
    Uses two helper methods: find_node and delete_node
    '''
    def __delitem__(self, key):
        victim, parent, is_left_child = self.find_node(key)

        if victim is None:
            raise KeyError
        else:
            self.delete_node(victim, parent, is_left_child)

    '''
    Given a node to delete, its parent, and its relationship to the parent,
    deletes the node.

    Method:
    case 1, victim is leaf: set parent's pointer to None
    case 2, victim is single parent: parent adopts victim's child
    case 3, victim has two children:
            a - swap contents with victim's successor
            b - delete successor
    '''
    def delete_node(self, victim, parent, is_left_child):
        if victim.is_leaf():
            if parent is None:
                self.root = None
            else:
                parent.del_child(is_left_child)
        elif victim.is_single_parent():
            if parent is None:
                # victim is root, and is single parent
                self.root = self.root.get_single_child()
            elif is_left_child:
                parent.left = victim.get_single_child()
            else:
                parent.right = victim.get_single_child()
        else:
            # victim has two children.
            # find successor
            succ, succ_parent, succ_is_left_child = self.next_on_right(victim)
            # swap contents of successor with victim
            # (but don't swap the child pointers!)
            victim.swap_data(succ)
            # and finally delete the sucessor
            self.delete_node(succ, succ_parent, succ_is_left_child)

    '''
    Helper method for __delete__.
    Walk down the tree (just like __contains__), but keep track
    of current node's parent and its parent-child relationship.
    '''
    def find_node(self, key):
        parent = None
        node = self.root
        is_left_child = True
        while node is not None:
            if node.key == key:
                return (node, parent, is_left_child)
            elif key < node.key:
                is_left_child = True
                parent = node
                node = node.left
            else:
                is_left_child = False
                parent = node
                node = node.right
        return (None,None,is_left_child)

    '''
    Successor of given node.
    Returns a triple: successor, its parent, its parent-child relationship
    '''
    def next_on_right(self, node):
        if node is None:
            return None,None,False
        elif node.right is None:
            return None,None,False
        else:
            parent = node
            is_left_child = False
            child = node.right
            while child.left is not None:
                parent = child
                child = child.left
                is_left_child = True
            return child, parent, is_left_child

    '''
    Counts number of nodes.
    Uses helper method
    '''
    def __len__(self):
        return self.size_of_subtree(self.root)

    '''
    Helper method for __len__
    '''
    def size_of_subtree(self, node):
        if node == None:
            return 0
        else:
            return 1 +\
                self.size_of_subtree(node.left) +\
                self.size_of_subtree(node.right)

    '''
    Stringify the tree, using the __iter__ method above.
    '''
    def __str__(self):
        if self.root is None:
            return '{}'
        else:
            result = '{'
            for x in self:
                result += str(x) + ' : ' + str(self[x]) + ', '
            return result[:-2] + '}'

    '''
    Programmer-friendly representation of tree.
    Uses helper method.
    '''
    def __repr__(self):
        result = 'BST(\n'
        result += self.reverse_inorder_repr(self.root, 0)
        result += ')'
        return result

    '''
    Helper for __repr__
    '''
    def reverse_inorder_repr(self, node, depth):
        if node != None:
            r_repr = self.reverse_inorder_repr(node.right, depth+1)
            l_repr = self.reverse_inorder_repr(node.left,  depth+1)
            return r_repr + \
                   '    ' + '  ' * depth + repr(node) + '\n' +\
                   l_repr
        else:
            return ''


    #############################################################
    #
    # The following methods will call the functions that YOU
    # must implement
    #
    #############################################################

    def predecessor(self, key):
        (node, parent, is_left_child) = self.find_node(key)
        node = preceding_node(node)
        if node == None:
            return (None, None)
        else:
            return (node.key, node.value)


    def print_inorder_and_depth(self):
        inorder_with_depth(self.root, 0)

    def print_indented(self):
        indented_print(self.root, 0)


    def max(self):
        return max_key(self.root)

    def min(self):
        return min_key(self.root)

    def is_bst(self):
        return is_root_of_bst(self.root)

    def has_path_sum(self, total):
        return has_path_sum(self.root, total)

######################################################################
#
# YOU MUST MODIFY THE FUNCTIONS BELOW THIS LINE
# (But look at the methods in the section just above,
#  to see how recursion starts)
#
# | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
# v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v

def preceding_node(node):
    # REPLACE THIS LINE:
    if node is None:
        return None
    elif node.left is None:
        return None
    else:
        child = node.left
        while node.right is not None:
            node = node.right
        return node

def inorder_with_depth(node, depth):
    if node is not None:
        inorder_with_depth(node.left,depth+1)
        print(node.key,depth)
        inorder_with_depth(node.right,depth+1)

def indented_print(node, depth):
    if node is not None:
        indented_print(node.left,depth+1)
        print("\t"*depth,node.key)
        indented_print(node.right,depth+1)

def max_key(node):
    if node is None:
        return 0
    else:
        maxLeft = max_key(node.left)
        maxRight = max_key(node.right)
        _max = max([maxLeft,maxRight,node.key])
        return _max

def min_key(node):
    if node is None:
        return int(1e6)
    else:
        minLeft = min_key(node.left)
        minRight = min_key(node.right)
        _min = min([minLeft,minRight,node.key])
        return _min

def is_root_of_bst(node):
    if node is None:
        return True
    else:
        # The "conditions" are given in lab19 PDF
        cond1 = max_key(node.left) < node.key
        cond2 = min_key(node.right) > node.key
        cond3 = is_root_of_bst(node.left)   # left size is bst
        cond4 = is_root_of_bst(node.right)  # right size is bst
        return (cond1 and cond2 and cond3 and cond4)


def has_path_sum(node, total):
    return None
        

# ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
# | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
#
# THE FUNCTIONS YOU MUST MODIFY ARE ABOVE THIS LINE
#
#######################################################################



def main():
    tree = BST()
    tree[3] = 'three'
    tree[1] = 'one'
    tree[4] = 'four'
    tree[1] = 'ein'
    tree[5] = 'five'
    tree[9] = 'nine'
    tree[2] = 'two',
    tree[6] = 'six'
    tree[5] = 'funf'
    tree[3] = 'drei'
    tree[5] = 'cinque'
    tree[8] = 'eight'
    tree[9] = 'neun'
    tree[7] = 'seven'
    tree[9] = 'neuf'
    tree[3] = 'trois'
    tree[2] = 'deux'
    tree[3] = 'tres'

    bad_tree = BST()
    node10 = Node(10)
    node5  = Node(5)
    node6  = Node(6)
    node7  = Node(7)
    node12 = Node(12)
    node11 = Node(11)
    node8  = Node(8)

    node10.left  = node5
    node10.right = node12

    node5.left   = node6
    node5.right  = node7

    node12.left  = node11
    node12.right = node8

    bad_tree.root = node10

    print( 'predecessor(3)  :', tree.predecessor(3) )
    print( 'predecessor(1)  :', tree.predecessor(1) )
    print( 'print with depth:\n' )
    tree.print_inorder_and_depth()
    print( 'print indented  :\n' )
    tree.print_indented()
    print( 'max             :', tree.max() )
    print( 'min             :', tree.min() )
    print( 'tree is BST     :', tree.is_bst() )
    print( 'bad tree is BST :', bad_tree.is_bst() )
    print( 'path adds to 6  :', tree.has_path_sum(6) )
    print( 'path adds to 42 :', tree.has_path_sum(42) )
    print( 'path adds to 11 :', tree.has_path_sum(11) )

if __name__ == '__main__':
    main()


