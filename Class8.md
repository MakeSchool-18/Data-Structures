### Class 8: Wednesday, April 5 – Trees

**Topics:**
- [tree], [terminology]
- [binary search tree], [operations][bst operations]

**Resources:**
- review Make School's [tree slides]
- watch Make School's [tree video lecture]
- play with VisuAlgo's [interactive binary search tree visualization][visualgo bst]

**Challenges:**
- implement `BinaryNode` class with the following properties and instance methods:
    - `data` - the node's data
    - `left` - the node's left child, if any
    - `right` - the node's right child, if any
    - `is_leaf` - check if the node is a leaf (has no children)
    - `is_internal` - check if the node is internal (has at least one child)
- implement `BinarySearchTree` class using `BinaryNode` objects with the following properties and instance methods:
    - `size` - property that tracks the number of nodes in constant time
    - `is_empty` - check if the tree is empty
    - `insert(data)` - insert a new node with `data` in order in the tree
    - `search(data)` - check if a node with `data` is present in the tree
    - `delete(data)` - remove the node with `data` from the tree
- write your own unit tests for your `BinarySearchTree` class
    - include test cases for each class instance method
- annotate all class instance methods with running time complexity analysis

**Stretch Challenges:**
- implement `TreeMap` class (map/dictionary abstract data type implemented with binary search tree data structure)
- implement binary search tree with singly linked list nodes instead of binary tree nodes

**Project:**
- [trees and mazes] tutorial on Make School's [Online Academy]

[tree]: https://en.wikipedia.org/wiki/Tree_(data_structure)
[terminology]: https://en.wikipedia.org/wiki/Tree_(data_structure)#Terminology_used_in_trees
[binary search tree]: https://en.wikipedia.org/wiki/Binary_search_tree
[bst operations]: https://en.wikipedia.org/wiki/Binary_search_tree#Operations

[tree slides]: slides/Trees.pdf
[tree video lecture]: https://www.youtube.com/watch?v=Yr3y78d2KYI
[visualgo bst]: https://visualgo.net/bst

[trees and mazes]: http://make.sc/oa-trees-and-mazes
[Online Academy]: https://www.makeschool.com/academy
