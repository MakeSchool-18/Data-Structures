#!python

class BinaryNode(object):

    def __init__(self, data):
        """Initialize this binary node with the given data"""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary node"""
        return 'BinaryNode({})'.format(repr(self.data))

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)"""
        # TODO: Check if both left child and right child have no value
        return ... and ...

    def is_internal(self):
        """Return True if this node is internal (has at least one child)"""
        # TODO: Check if either left child or right child has a value
        return ... or ...

    def height(self):
        """Return the number of edges on the longest downward path from this
        node to a descendant leaf node"""
        # TODO: Check if left child has a value and if so calculate its height
        left_height = ... if self.left is not None else -1
        # TODO: Check if right child has a value and if so calculate its height
        right_height = ... if self.right is not None else -1
        # Return one more than the greater of the left height and right height
        return 1 + max(left_height, right_height)


class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items"""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree"""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree contains no nodes"""
        return self.root is None

    def height(self):
        """Return the number of edges on the longest downward path from this
        tree's root node to a descendant leaf node (the height of the root)"""
        # Check if root node has a value and if so calculate its height
        return self.root.height() if self.root is not None else -1

    def contains(self, item):
        """Return True if this binary search tree contains the given item"""
        # Find a node with the given item, if any
        node = self._find_node(item)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item"""
        # Find a node with the given item, if any
        node = self._find_node(item)
        # TODO: Return the node's data if found, or None
        return node.data if ... else None

    def _find_node(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found"""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            # TODO: Check if the given item matches the node's data
            if ...:
                # Return the found node
                return node
            # TODO: Check if the given item is less than the node's data
            elif ...:
                # TODO: Descend to the node's left child
                node = ...
            # TODO: Check if the given item is greater than the node's data
            elif ...:
                # TODO: Descend to the node's right child
                node = ...
        # Not found
        return None

    def _find_parent_node(self, item):
        """Return the parent node of where the given item is (or would be) in
        this binary search tree, or None if this tree has only a root node"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            # TODO: Check if the given item matches the node's data
            if ...:
                # Return the parent of the found node
                return parent
            # TODO: Check if the given item is less than the node's data
            elif ...:
                # TODO: Update the parent and descend to the node's left child
                parent = node
                node = ...
            # TODO: Check if the given item is greater than the node's data
            elif ...:
                # TODO: Update the parent and descend to the node's right child
                parent = node
                node = ...
        # Not found
        return parent

    def insert(self, item):
        """Insert the given item in order into this binary search tree"""
        # Handle the case where the tree is empty
        if self.is_empty():
        # if self.root is None:
            # TODO: Create a new root node
            self.root = ...
            # TODO: Increase the tree size
            self.size ...
            return
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node(item)
        # TODO: Check if the given item should be inserted left of the parent node
        if ...:
            # TODO: Create a new node and set the parent's left child
            parent.left = ...
        # TODO: Check if the given item should be inserted right of the parent node
        elif ...:
            # TODO: Create a new node and set the parent's right child
            parent.right = ...
        # TODO: Increase the tree size
        self.size ...


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: ' + str(items))

    bst = BinarySearchTree()
    print('tree: ' + str(bst))
    print('root: ' + str(bst.root))

    print('\nInserting items:')
    for item in items:
        bst.insert(item)
        # print('insert({})'.format(item))
        print('insert({}), size: {}'.format(item, bst.size))
        # print(bst)
    print('root: ' + str(bst.root))

    print('\nSearching for items:')
    for item in items:
        result = bst.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = bst.search(item)
    print('search({}): {}'.format(item, result))


if __name__ == '__main__':
    test_binary_search_tree()
