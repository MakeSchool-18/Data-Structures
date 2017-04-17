### Class 13: Monday, April 17 – Recursive Algorithm Analysis

**Topics:**
- recursive algorithm analysis with trees, [recurrence relations], [master theorem]
- partition algorithm and [quick sort]
- how to [choose a pivot]: first, last, middle, median-of-three, random
- partitioning schemes: [Lomuto], [Hoare], or [three-way]
- sorting algorithm [stability]
- [in-place] algorithms

**Resources:**
- review Make School's [recursive algorithm analysis slides]
- watch these cute robot video animations: [quick sort][video quick sort], [merge sort vs. quick sort][video merge quick sort]
- read Sebastian's answer to this [quick sort partitioning] question on Computer Science Stack Exchange
- play with USF's [interactive sorting animations] to follow algorithms step-by-step
- watch Toptal's [sorting animations] to see how algorithms compare based on input data and read the discussion section
- watch videos to observe patterns: [9 sorting algorithms], [15 sorting algorithms], [23 sorting algorithms]

**Challenges:**
- implement partition algorithm that chooses a pivot and segments a list into sublists
    - `partition(items)` - return a pair of lists `(small, large)` containing all elements less than (or equal to) pivot in `small` and all elements greater than pivot in `large`
    - [choose a pivot] in any way: first, last, middle, median-of-three, random
    - use any partitioning scheme: [Lomuto], [Hoare], or [three-way] (return a triple)
- implement recursive quick sort that uses `partition` algorithm and sorts sublists recursively
    - `quick_sort(items)` - return a list containing all elements of `items` in sorted order
    - use the [divide-and-conquer] problem-solving strategy:
        1. **Divide:** split problem into subproblems (partition input list into sublists)
        2. **Conquer:** solve subproblems independently (sort sublists recursively with quick sort)
        3. **Combine:** combine subproblem solutions together (concatenate sorted sublists)
    - remember to add a base case to avoid infinite recursion loops (*hint:* very small lists are always sorted)
- annotate your `partition` and `quick_sort` functions with complexity analysis
- write unit tests for your sorting algorithms
    - include test cases of varying sizes and edge cases

**Stretch Challenges:**
- try other techniques to choose a pivot and other partitioning algorithms
- implement *in-place* quick sort with a separate *in-place* partition algorithm
- implement *stable* quick sort with a separate *stable* partition algorithm
- implement [slow sort] algorithm, just for fun ;-)
- annotate functions with complexity analysis

**Project:**
- [sorting algorithms] with real-world data on Make School's Online Academy

[recurrence relations]: https://en.wikipedia.org/wiki/Recurrence_relation
[master theorem]: https://en.wikipedia.org/wiki/Master_theorem
[quick sort]: https://en.wikipedia.org/wiki/Quicksort
[choose a pivot]: https://en.wikipedia.org/wiki/Quicksort#Choice_of_pivot
[Lomuto]: https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme
[Hoare]: https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme
[three-way]: https://en.wikipedia.org/wiki/Dutch_national_flag_problem
[slow sort]: https://en.wikipedia.org/wiki/Slowsort
[stability]: https://en.wikipedia.org/wiki/Sorting_algorithm#Stability
[in-place]: https://en.wikipedia.org/wiki/In-place_algorithm

[recursive algorithm analysis slides]: slides/AlgorithmAnalysisRecursive.pdf
[video quick sort]: https://www.youtube.com/watch?v=aXXWXz5rF64
[video merge quick sort]: https://www.youtube.com/watch?v=es2T6KY45cA
[quick sort partitioning]: https://cs.stackexchange.com/questions/11458/quicksort-partitioning-hoare-vs-lomuto
[sorting animations]: https://www.toptal.com/developers/sorting-algorithms/
[interactive sorting animations]: https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html
[3 sorting algorithms]: https://www.youtube.com/watch?v=jHPexHsDxwQ
[9 sorting algorithms]: https://www.youtube.com/watch?v=ZZuD6iUe3Pc
[15 sorting algorithms]: https://www.youtube.com/watch?v=kPRA0W1kECg
[23 sorting algorithms]: https://www.youtube.com/watch?v=rqI6KT6cOas

[sorting algorithms]: http://make.sc/oa-sorting-algorithms
