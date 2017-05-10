### Class 20: Wednesday, May 10 – Trie & Multiple Key Trees

**Topics:**
- [*k*-ary tree (*n*-ary tree, *m*-way tree)][k-ary tree]
- [trie (prefix tree, radix tree)][trie]
- [self-balancing trees] with multiple keys: [2-3 tree], [B-tree]
<!-- - [space-partitioning] trees: [quadtree], [octree], [k-d tree] -->

**Resources:**
- review Julia Geist's [trie slides] with animations and examples
- read Julia Geist's [trie article] with animations and code samples
- play with USF's [interactive trie animations][USF trie]
- review Alex Dejeu's [B-tree slides] with examples and motivating context
- read Alex Dejeu's [2-3 tree article] with animations and code samples
- watch MIT's [2-3 tree and B-tree video lecture]
- play with USF's [interactive B-tree animations][USF B-tree]

**Challenges:**
- implement `TwoThreeNode` class with the following properties and instance methods using [Alex's 2-3 tree starter code]:
    - `data` - the node's list of data
    - `children` - the node's list of children, if any
    - `parent` - the node's parent, if not the root
    - `add_data(data)` - insert `data` in order in the node's list of data
    - `is_full` - check if the node is full (has at least 3 data)
    - `has_space` - check if the node has space (has only 1 datum)
    - `is_leaf` - check if the node is a leaf (has no children)
    - `is_internal` - check if the node is internal (has at least one child)
- implement `TwoThreeTree` class using `TwoThreeNode` objects with the following properties and instance methods using [Alex's 2-3 tree starter code]:
    - `root` - the tree's root node
    - `is_empty` - check if the tree is empty
    - `insert(data)` - insert a new node with `data` in order in the tree
    - `search(data)` - check if a node with `data` is present in the tree
    - `find_node(data)` - return the node where `item` is (or would be) in the tree, or None
    - `split_node(node)` - split `node` to promote its median element and follow the path up to the tree's root and perform any more splits necessary
    - `items_in_order` - return a list of all items in the tree found using in-order traversal
    - `items_level_order` - return a list of all items in the tree found using level-order traversal
- run `pytest test_two_three_tree.py` to run [Alex's 2-3 tree unit tests] and fix any failures
- annotate class instance methods with complexity analysis

**Stretch Challenges:**
- implement trie with insert and prefix search operations
- revisit [phone call routing] scenarios 3, 4, and 5 with trie
- annotate class instance methods with complexity analysis

[k-ary tree]: https://en.wikipedia.org/wiki/K-ary_tree
[trie]: https://en.wikipedia.org/wiki/Trie
[self-balancing trees]: https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree
[2-3 tree]: https://en.wikipedia.org/wiki/2%E2%80%933_tree
[B-tree]: https://en.wikipedia.org/wiki/B-tree

[space-partitioning]: https://en.wikipedia.org/wiki/Space_partitioning
[quadtree]: https://en.wikipedia.org/wiki/Quadtree
[octree]: https://en.wikipedia.org/wiki/Octree
[k-d tree]: https://en.wikipedia.org/wiki/K-d_tree

[trie slides]: https://docs.google.com/presentation/d/11LDrlureRaXyg6ZfjgJvdMZohLfk-0JYuB1RW2xVZDE/edit#slide=id.p
[trie article]: https://medium.com/algorithms/trie-prefix-tree-algorithm-ee7ab3fe3413
[Julia trie article]: http://juliageist.com/blog/algorithms-and-data-structures/trie-prefix-tree/
[B-tree slides]: slides/B-Trees.pdf
[2-3 tree article]: https://medium.com/@alexdejeu/9b50e3484a47
[2-3 tree and B-tree video lecture]: https://www.youtube.com/watch?v=TOb1tuEZ2X4
[USF trie]: https://www.cs.usfca.edu/~galles/visualization/Trie.html
[USF B-tree]: https://www.cs.usfca.edu/~galles/visualization/BTree.html

[Alex's 2-3 tree starter code]: https://github.com/alexander-dejeu/CodeForMediumArticles/blob/master/two_three_tree.py
[Alex's 2-3 tree unit tests]: https://github.com/alexander-dejeu/CodeForMediumArticles/blob/master/test_two_three_tree.py

[phone call routing]: http://make.sc/db-phone-call-routing
