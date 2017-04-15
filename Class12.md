### Class 12: Friday, April 14 – Divide-and-Conquer Recursion

**Topics:**
- [divide-and-conquer]&nbsp;[recursion]: divide, conquer, combine
- revisit [binary search] to see how it divides and conquers
- [merge algorithm] and [merge sort]

**Resources:**
- read Brian Hans's [merge sort article] with animations and pseudocode
- play with USF's [interactive sorting animations] to follow algorithms step-by-step
- watch Toptal's [sorting animations] to see how algorithms compare based on input data and read the discussion section
- watch videos to observe patterns: [9 sorting algorithms], [15 sorting algorithms], [23 sorting algorithms]

**Challenges:**
- implement merge algorithm that combines two sorted lists into one sorted list
    - `merge(list1, list2)` - return a list containing all elements in order from `list1` and `list2`, which are assumed to be in order
- implement *non-recursive* merge sort that uses any *other* sorting algorithm to sort sublists
    - `merge_sort(items)` - return a list containing all elements of `items` in sorted order
    - use the [divide-and-conquer] problem-solving strategy:
        1. **Divide:** split problem (input list) into subproblems (two sublists of half size)
        2. **Conquer:** solve subproblems independently (sort sublists with any sorting algorithm)
        3. **Combine:** combine subproblem solutions together (merge sorted sublists)
- implement *recursive* merge sort that calls *itself* to sort sublists recursively
    - remember to add a base case to avoid infinite recursion loops (*hint:* very small lists are always sorted)
- annotate your `merge` and non-recursive `merge_sort` functions with complexity analysis
- write unit tests for your sorting algorithms
    - include test cases of varying sizes and edge cases

**Stretch Challenges:**
- implement [bucket sort] for integers using a divide-and-conquer recursive style

**Project:**
- [sorting algorithms] with real-world data on Make School's Online Academy

[divide-and-conquer]: https://en.wikipedia.org/wiki/Divide_and_conquer_algorithm
[recursion]: https://en.wikipedia.org/wiki/Recursion_(computer_science)
[binary search]: https://en.wikipedia.org/wiki/Binary_search_algorithm
[merge algorithm]: https://en.wikipedia.org/wiki/Merge_algorithm
[merge sort]: https://en.wikipedia.org/wiki/Merge_sort
[bucket sort]: https://en.wikipedia.org/wiki/Bucket_sort

[merge sort article]: https://medium.com/@brianhans/merge-sort-a1d031eaa40f
[sorting animations]: https://www.toptal.com/developers/sorting-algorithms/
[interactive sorting animations]: https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html
[3 sorting algorithms]: https://www.youtube.com/watch?v=jHPexHsDxwQ
[9 sorting algorithms]: https://www.youtube.com/watch?v=ZZuD6iUe3Pc
[15 sorting algorithms]: https://www.youtube.com/watch?v=kPRA0W1kECg
[23 sorting algorithms]: https://www.youtube.com/watch?v=rqI6KT6cOas

[sorting algorithms]: http://make.sc/oa-sorting-algorithms
