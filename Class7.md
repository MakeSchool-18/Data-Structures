### Class 7: Monday, April 3 – Set & Circular Buffer

**Topics:**
- abstract data types: [set], [multiset (bag)][multiset]
- concrete data structures: [hash table], [circular buffer]
- [set operations]

**Challenges:**
- implement `HashSet` class (set with hash table) with the following [set operations] as instance methods and properties:
    - `__init__(elements=None)` - initialize a new empty set structure, and add each element if a sequence is given
    - `size` - property that tracks the number of elements in constant time
    - `contains(element)` - check whether `element` is in this set
    - `add(element)` - add `element` to this set, if not present already
    - `remove(element)` - remove `element` from this set, if present
    - `union(other_set)` - return the union of this set and `other_set`
    - `intersection(other_set)` - return the intersection of this set and `other_set`
    - `difference(other_set)` - return the difference of this set and `other_set`
    - `is_subset(other_set)` - check whether `other_set` is a subset of this set
- write your own unit tests for your `HashSet` class
    - include test cases for each class instance method
- annotate all class instance methods with running time complexity analysis

**Stretch Challenges:**
- implement `CircularBuffer` class with dynamic array
- write your own unit tests for your `CircularBuffer` class
    - include test cases for each class instance method
- annotate all class instance methods with running time complexity analysis

[set]: https://en.wikipedia.org/wiki/Set_(abstract_data_type)
[multiset]: https://en.wikipedia.org/wiki/Set_(abstract_data_type)#Multiset
[set operations]: https://en.wikipedia.org/wiki/Set_(abstract_data_type)#Operations
[hash table]: https://en.wikipedia.org/wiki/Hash_table
[circular buffer]: https://en.wikipedia.org/wiki/Circular_buffer
