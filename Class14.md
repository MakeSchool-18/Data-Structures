### Class 14: Wednesday, April 19 – Priority Queue & Heap

**Topics:**
- [priority queue] abstract data type, implementations: unsorted list, sorted list, [bucket queue]
- [heap] data structure, [binary heap] representations: binary tree, array
- [heap sort], compare to [insertion sort] and [selection sort]
- sorting algorithm [stability]
- [in-place] algorithms

**Resources:**
- review Make School's [heap slides]
- watch Make School's [heap video lecture]
- watch this cute robot [heap sort animation video]
- play with VisuAlgo's [interactive heap visualization][visualgo heap]
- read about [sorting algorithms implemented with priority queue][priority queue sorting]

**Challenges:**
- implement `MinHeap` class using dynamic array with the following instance methods using [heap starter code]:
    - `is_empty` - check if the heap is empty
    - `size` - return the number of items in the heap
    - `get_min` - return the minimum item at the root of the heap
    - `remove_min` - remove and return the minimum item at the root of the heap
    - `replace_min(item)` - remove and return the minimum item, and insert `item` into this heap
    - `insert(item)` - insert `item` into this heap
    - `_bubble_up(index)` - ensure the heap-ordering property is true above `index`, swapping out of order items
    - `_bubble_down(index)` - ensure the heap-ordering property is true below `index`, swapping out of order items
- run `pytest test_heap.py` to run the [heap unit tests] and fix any failures
- implement heap sort with binary heap (this is *super* easy)
- implement `PriorityQueue` class using binary heap with the following instance methods using [priority queue starter code]:
    - `is_empty` - check if the priority queue is empty
    - `length` - return the number of items in the priority queue
    - `enqueue(item, priority)` - insert `item` into the priority queue in order according to `priority`
    - `front` - return the item at the front of the priority queue without removing it, or None
    - `dequeue` - remove and return the item at the front of the priority queue, or raise ValueError
    - `push_pop(item, priority)` - remove and return the item at the front of this priority queue, and insert `item` in order according to `priority`
- annotate class instance methods with running time complexity analysis

**Stretch Challenges:**
- implement priority queue with binary search tree
- implement stack with priority queue
- generalize binary heap with min or max initialization option

[priority queue]: https://en.wikipedia.org/wiki/Priority_queue
[bucket queue]: https://en.wikipedia.org/wiki/Bucket_queue
[heap]: https://en.wikipedia.org/wiki/Heap_(data_structure)
[binary heap]: https://en.wikipedia.org/wiki/Binary_heap
[heap sort]: https://en.wikipedia.org/wiki/Heapsort
[insertion sort]: https://en.wikipedia.org/wiki/Insertion_sort
[selection sort]: https://en.wikipedia.org/wiki/Selection_sort
[priority queue sorting]: https://en.wikipedia.org/wiki/Priority_queue#Equivalence_of_priority_queues_and_sorting_algorithms
[stability]: https://en.wikipedia.org/wiki/Sorting_algorithm#Stability
[in-place]: https://en.wikipedia.org/wiki/In-place_algorithm

[heap slides]: slides/Heaps.pdf
[heap video lecture]: https://www.youtube.com/watch?v=eBGgEEXnbuk
[heap sort animation video]: https://www.youtube.com/watch?v=H5kAcmGOn4Q
[visualgo heap]: https://visualgo.net/heap

[heap starter code]: source/heap.py
[heap unit tests]: source/test_heap.py
[priority queue starter code]: source/priorityqueue.py
