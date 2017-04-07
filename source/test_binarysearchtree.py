#!python

from binarysearchtree import BinarySearchTree, BinaryNode
import unittest


class TestBinaryNode(unittest.TestCase):

    def test_init(self):
        data = 123
        node = BinaryNode(data)
        assert node.data is data
        assert node.left is None
        assert node.right is None


class TestBinarySearchTree(unittest.TestCase):

    def test_init(self):
        bst = BinarySearchTree()
        assert bst.root is None
        assert bst.size == 0
        assert bst.is_empty() is True

    def test_init_with_list(self):
        bst = BinarySearchTree([2, 1, 3])
        assert bst.root.data == 2
        assert bst.root.left.data == 1
        assert bst.root.right.data == 3
        assert bst.size == 3
        assert bst.is_empty() is False

    def test_init_with_list_of_strings(self):
        bst = BinarySearchTree(['B', 'A', 'C'])
        assert bst.root.data == 'B'
        assert bst.root.left.data == 'A'
        assert bst.root.right.data == 'C'
        assert bst.size == 3
        assert bst.is_empty() is False

    def test_init_with_list_of_tuples(self):
        bst = BinarySearchTree([(2, 'B'), (1, 'A'), (3, 'C')])
        assert bst.root.data == (2, 'B')
        assert bst.root.left.data == (1, 'A')
        assert bst.root.right.data == (3, 'C')
        assert bst.size == 3
        assert bst.is_empty() is False

    def test_size(self):
        bst = BinarySearchTree()
        assert bst.size == 0
        bst.insert('B')
        assert bst.size == 1
        bst.insert('A')
        assert bst.size == 2
        bst.insert('C')
        assert bst.size == 3

    def test_search_with_3_items(self):
        # Create a complete binary search tree of 3 items in level-order
        items = [2, 1, 3]
        bst = BinarySearchTree(items)
        assert bst.search(1) == 1
        assert bst.search(2) == 2
        assert bst.search(3) == 3
        assert bst.search(4) is None

    def test_search_with_7_items(self):
        # Create a complete binary search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        bst = BinarySearchTree(items)
        for item in items:
            assert bst.search(item) == item
        assert bst.search(8) is None

    def test_search_with_3_strings(self):
        # Create a complete binary search tree of 3 items in level-order
        items = ['B', 'A', 'C']
        bst = BinarySearchTree(items)
        assert bst.search('A') == 'A'
        assert bst.search('B') == 'B'
        assert bst.search('C') == 'C'
        assert bst.search('D') is None

    def test_search_with_7_strings(self):
        # Create a complete binary search tree of 7 items in level-order
        items = ['D', 'B', 'F', 'A', 'C', 'E', 'G']
        bst = BinarySearchTree(items)
        for item in items:
            assert bst.search(item) == item
        assert bst.search('H') is None

    def test_insert_with_3_items(self):
        # Create a complete binary search tree of 3 items in level-order
        bst = BinarySearchTree()
        bst.insert(2)
        assert bst.root.data == 2
        assert bst.root.left is None
        assert bst.root.right is None
        bst.insert(1)
        assert bst.root.data == 2
        assert bst.root.left.data == 1
        assert bst.root.right is None
        bst.insert(3)
        assert bst.root.data == 2
        assert bst.root.left.data == 1
        assert bst.root.right.data == 3

    def test_insert_with_7_items(self):
        # Create a complete binary search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        bst = BinarySearchTree()
        for item in items:
            bst.insert(item)
        assert bst.root.data == 4
        assert bst.root.left.data == 2
        assert bst.root.right.data == 6
        assert bst.root.left.left.data == 1
        assert bst.root.left.right.data == 3
        assert bst.root.right.left.data == 5
        assert bst.root.right.right.data == 7


if __name__ == '__main__':
    unittest.main()
