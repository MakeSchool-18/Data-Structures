### Class 4: Monday, March 27 –  List, Array & Linked List

**Topics:**
- compare [abstract data types] and [concrete data structures][data structures]
- abstract data types: [list]
- concrete data structures: [array], [dynamic array (resizable array, vector)][dynamic array], [linked list]

**Resources:**
- review Make School's [array and linked list slides][list slides]
- watch Make School's [array and linked list video lecture][list video]
- play with VisuAlgo's [interactive linked list visualization][visualgo list]

**Challenges:**
- add new features to `LinkedList` class using [linked list starter code]:
    - add `size` property that tracks list length in constant running time
    - implement `get_at_index(index)` - returns the item at `index` in the list
    - implement `insert_at_index(index, item)` - inserts `item` at `index` (all items after `index` are moved down)
    - run `python linkedlist.py` to test `LinkedList` class instance methods on a small example
    - run `pytest test_linkedlist.py` to run the [linked list unit tests] and fix any failures
- annotate functions with complexity analysis

**Stretch Challenges:**
- implement `DoublyLinkedList` class with `BinaryNode` objects, which have both `next` and `previous` properties
- write your own unit tests for your `DoublyLinkedList` class
    - include test cases for each class instance method
- annotate functions with complexity analysis

[abstract data types]: https://en.wikipedia.org/wiki/Abstract_data_type
[data structures]: https://en.wikipedia.org/wiki/Data_structure
[list]: https://en.wikipedia.org/wiki/List_(abstract_data_type)
[array]: https://en.wikipedia.org/wiki/Array_data_structure
[dynamic array]: https://en.wikipedia.org/wiki/Dynamic_array
[linked list]: https://en.wikipedia.org/wiki/Linked_list

[list slides]: slides/ArraysLinkedLists.pdf
[list video]: https://www.youtube.com/watch?v=3WWuf4H61Nk
[visualgo list]: https://visualgo.net/list

[linked list starter code]: source/linkedlist.py
[linked list unit tests]: source/test_linkedlist.py
