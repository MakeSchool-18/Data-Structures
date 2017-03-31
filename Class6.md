### Class 6: Friday, March 31 – Map & Hash Table

**Topics:**
- abstract data types: [map (dictionary, associative array)][map]
- concrete data structures: [hash table]
- [hash functions], [collision resolution], [load factor], [dynamic resizing]

**Resources:**
- review Make School's [hash table slides]
- watch Make School's [hash table video lecture]
- play with VisuAlgo's [interactive hash table visualization][visualgo hash table]

**Challenges:**
- add new features to improve `HashTable` class using [hash table starter code]:
    - add `size` property that tracks the number of hash table entries in constant time
    - implement `load_factor` - return the [load factor], the ratio of number of entries to buckets
    - implement `_resize` - perform [dynamic resizing] when `load_factor` exceeds `0.75` after an insertion (`set` is called with a new `key`) and rehash all key-value entries
    - run `python hashtable.py` to test `HashTable` class instance methods on a small example
    - run `pytest test_hashtable.py` to run the [hash table unit tests] and fix any failures
- annotate new class instance methods with running time complexity analysis

**Stretch Challenges:**
- implement hash table [collision resolution] with [linear probing] instead of [separate chaining]

[map]: https://en.wikipedia.org/wiki/Associative_array
[hash table]: https://en.wikipedia.org/wiki/Hash_table
[hash functions]: https://en.wikipedia.org/wiki/Hash_function
[load factor]: https://en.wikipedia.org/wiki/Hash_table#Key_statistics
[dynamic resizing]: https://en.wikipedia.org/wiki/Hash_table#Dynamic_resizing
[collision resolution]: https://en.wikipedia.org/wiki/Hash_table#Collision_resolution
[separate chaining]: https://en.wikipedia.org/wiki/Hash_table#Separate_chaining
[linear probing]: https://en.wikipedia.org/wiki/Linear_probing

[hash table slides]: slides/HashTables.pdf
[hash table video lecture]: https://www.youtube.com/watch?v=nLWXJ6IDKmQ
[visualgo hash table]: https://visualgo.net/hashtable

[hash table starter code]: source/hashtable.py
[hash table unit tests]: source/test_hashtable.py
