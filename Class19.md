### Class 19: Monday, May 8 – Rotating Binary Search Trees

**Topics:**
- [self-balancing binary search trees] with [rotations]: [AVL tree], [splay tree]

**Resources:**
- review Julia Geist's [AVL tree slides] with animations and examples
- read Julia Geist's [AVL tree article] with animations and code samples
- watch MIT's [AVL tree video lecture]
- play with VisuAlgo's [interactive AVL tree visualization][visualgo bst] to follow rotations step-by-step
- play with USF's [interactive AVL tree animations][USF AVL tree]
- play with USF's [interactive splay tree animations][USF splay tree]

**Challenges:**
- implement `AVLNode` class with the following properties and instance methods using [Julia's AVL tree starter code]:
    - `data` - the node's data
    - `left` - the node's left child, if any
    - `right` - the node's right child, if any
    - `parent` - the node's parent, if not the root
    - `height` - the node's height (the number of edges on the longest downward path to a descendant leaf node)
    - `update_height` - recalculate height based on left child's height and right child's height
    - `balance_factor` - return the difference between left child's height and right child's height
- implement `AVLTree` class using `AVLNode` objects with the following properties and instance methods using [Julia's AVL tree starter code]:
    - `root` - the tree's root node
    - `is_empty` - check if the tree is empty
    - `insert(data)` - insert a new node with `data` in order in the tree
    - `search(data)` - check if a node with `data` is present in the tree
    - `retrace_up(node)` - retrace the path from `node` up to the tree's root and perform any rotations necessary to rebalance
    - `rotate_left(node)` - rotate `node`'s right child so `node` becomes its left child
    - `rotate_right(node)` - rotate `node`'s left child so `node` becomes its right child
    - `items_in_order` - return a list of all items in the tree found using in-order traversal
    - `items_level_order` - return a list of all items in the tree found using level-order traversal
- run `pytest test_avl_tree.py` to run [Julia's AVL tree unit tests] and fix any failures
- annotate class instance methods with complexity analysis

**Stretch Challenges:**
- implement splay tree with insert and search operations
- annotate class instance methods with complexity analysis

[self-balancing binary search trees]: https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree
[rotations]: https://en.wikipedia.org/wiki/Tree_rotation
[AVL tree]: https://en.wikipedia.org/wiki/AVL_tree
[splay tree]: https://en.wikipedia.org/wiki/Splay_tree
[red-black tree]: https://en.wikipedia.org/wiki/Red%E2%80%93black_tree

[AVL tree slides]: https://docs.google.com/presentation/d/1ZTq_DbxTpnnTMw5GvF4TNJZV7P0k1UGwmm40-SBgfM8/edit
[AVL tree article]: https://medium.com/@julia.geist/c8cef61d3ea1
[AVL tree video lecture]: https://www.youtube.com/watch?v=FNeL18KsWPc
[visualgo bst]: https://visualgo.net/bst
[USF AVL tree]: https://www.cs.usfca.edu/~galles/visualization/AVLtree.html
[USF splay tree]: https://www.cs.usfca.edu/~galles/visualization/SplayTree.html
[USF red-black tree]: https://www.cs.usfca.edu/~galles/visualization/RedBlack.html

[Julia's AVL tree starter code]: https://github.com/juliascript/AVLTrees/blob/master/starter_avl_tree.py
[Julia's AVL tree unit tests]: https://github.com/juliascript/AVLTrees/blob/master/test_avl_tree.py
