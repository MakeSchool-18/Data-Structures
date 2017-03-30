### Class 5: Wednesday, March 29 – List, Stack & Queue

**Topics:**
- compare [abstract data types] and [concrete data structures][data structures]
- abstract data types: [list], [stack], [queue], [deque]
- concrete data structures: [array], [dynamic array (resizable array, vector)][dynamic array], [linked list]

**Resources:**
- review Make School's [stack and queue slides]
- watch Make School's [stack and queue video lecture]
- play with VisuAlgo's [interactive stack and queue visualization][visualgo list]

**Challenges:**
- implement `LinkedStack` class (stack with linked list) and `ArrayStack` class (stack with dynamic array) using [stack starter code]:
    - implement `is_empty` - check if the stack is empty
    - implement `length` - return the number of items in the stack
    - implement `push(item)` - insert `item` on the top of the stack
    - implement `peek` - return the item on the top of the stack
    - implement `pop` - remove and return the item on the top of the stack
    - run `pytest test_stack.py` to run the [stack unit tests] and fix any failures
- implement `LinkedQueue` class (queue with linked list) and `ArrayQueue` class (queue with dynamic array) using [queue starter code]:
    - implement `is_empty` - check if the queue is empty
    - implement `length` - return the number of items in the queue
    - implement `enqueue(item)` - insert `item` at the back of the queue
    - implement `front` - return the item at the front of the queue
    - implement `dequeue` - remove and return the item at the front of the queue
    - run `pytest test_queue.py` to run the [queue unit tests] and fix any failures
- annotate all class instance methods with running time complexity analysis

**Stretch Challenges:**
- implement `Deque` class with doubly linked list:
    - implement `is_empty` - check if the deque is empty
    - implement `length` - return the number of items in the deque
    - implement `push_front(item)` - insert `item` at the front of the deque
    - implement `push_back(item)` - insert `item` at the back of the deque
    - implement `front` - return the item at the front of the deque
    - implement `back` - return the item at the back of the deque
    - implement `pop_front` - remove and return the item at the front of the deque
    - implement `pop_back` - remove and return the item at the back of the deque
- write your own unit tests for your `Deque` class
    - include test cases for each class instance method
- annotate functions with complexity analysis

[abstract data types]: https://en.wikipedia.org/wiki/Abstract_data_type
[data structures]: https://en.wikipedia.org/wiki/Data_structure
[list]: https://en.wikipedia.org/wiki/List_(abstract_data_type)
[stack]: https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
[queue]: https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
[deque]: https://en.wikipedia.org/wiki/Double-ended_queue
[array]: https://en.wikipedia.org/wiki/Array_data_structure
[dynamic array]: https://en.wikipedia.org/wiki/Dynamic_array
[linked list]: https://en.wikipedia.org/wiki/Linked_list

[stack and queue slides]: slides/StacksQueues.pdf
[stack and queue video lecture]: https://www.youtube.com/watch?v=AXWnk4gege4
[visualgo list]: https://visualgo.net/list

[stack starter code]: source/stack.py
[stack unit tests]: source/test_stack.py
[queue starter code]: source/queue.py
[queue unit tests]: source/test_queue.py
