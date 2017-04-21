### Class 15: Friday, April 21 – Sorting Algorithms Recap

**Topics:**
- [hybrid] sorting algorithms: [introsort], [Timsort]
- ideal sorting algorithm features: [stable], [adaptive], [in-place]

**[Comparison Sorting] Algorithm Complexity**

| Algorithm        | Best Time        | Average Time     | Worst Time       | Worst Space | Features                   |
| ---------------- | ---------------- | ---------------- | ---------------- | ----------- | -------------------------- |
| [Bubble sort]    | Ω(n)             | Θ(n<sup>2</sup>) | O(n<sup>2</sup>) | O(1)        | stable, in-place, adaptive |
| [Selection sort] | Ω(n<sup>2</sup>) | Θ(n<sup>2</sup>) | O(n<sup>2</sup>) | O(1)        | stable, in-place           |
| [Insertion sort] | Ω(n)             | Θ(n<sup>2</sup>) | O(n<sup>2</sup>) | O(1)        | stable, in-place, adaptive |
| [Tree sort]      | Ω(n log(n))      | Θ(n log(n))      | O(n<sup>2</sup>) | O(n)        |                            |
| [Quick sort]     | Ω(n log(n))      | Θ(n log(n))      | O(n<sup>2</sup>) | O(log(n))   | in-place                   |
| [Merge sort]     | Ω(n log(n))      | Θ(n log(n))      | O(n log(n))      | O(n)        | stable                     |
| [Heap sort]      | Ω(n log(n))      | Θ(n log(n))      | O(n log(n))      | O(1)        | in-place                   |
| [Introsort]      | Ω(n log(n))      | Θ(n log(n))      | O(n log(n))      | O(log(n))   | hybrid, in-place           |
| [Timsort]        | Ω(n)             | Θ(n log(n))      | O(n log(n))      | O(n)        | hybrid, stable, adaptive   |

**[Integer Sorting] Algorithm Complexity**

| Algorithm       | Best Time | Average Time | Worst Time       | Worst Space |
| --------------- | --------- | ------------ | ---------------- | ----------- |
| [Counting sort] | Ω(n+k)    | Θ(n+k)       | O(n+k)           | O(k)        |
| [Bucket sort]   | Ω(n+k)    | Θ(n+k)       | O(n<sup>2</sup>) | O(n)        |
| [Radix sort]    | Ω(nk)     | Θ(nk)        | O(nk)            | O(n+k)      |

**Resources:**
- play with USF's [interactive sorting animations] to follow algorithms step-by-step
- watch Toptal's [sorting animations] to see how algorithms compare based on input data and read the discussion section
- watch TutorialsCC's [sorting algorithm videos] to observe patterns, especially the [Timsort video]
- watch people perform [sorting algorithms with folk dances], especially [merge sort with German folk dance] and [quick sort with Hungarian folk dance]
- watch University of Toronto's "[Sorting Out Sorting]" 30-minute film from 1981
- download Timo Bingmann's [The Sound of Sorting] software to hear and visualize sorting algorithms

**Project:**
- [sorting algorithms] with real-world data on Make School's Online Academy

[sorting algorithm]: https://en.wikipedia.org/wiki/Sorting_algorithm
[stable]: https://en.wikipedia.org/wiki/Sorting_algorithm#Stability
[adaptive]: https://en.wikipedia.org/wiki/Adaptive_sort
[in-place]: https://en.wikipedia.org/wiki/In-place_algorithm
[hybrid]: https://en.wikipedia.org/wiki/Hybrid_algorithm

[comparison sorting]: https://en.wikipedia.org/wiki/Comparison_sort
[bubble sort]: https://en.wikipedia.org/wiki/Bubble_sort
[selection sort]: https://en.wikipedia.org/wiki/Selection_sort
[insertion sort]: https://en.wikipedia.org/wiki/Insertion_sort

[tree sort]: https://en.wikipedia.org/wiki/Tree_sort
[quick sort]: https://en.wikipedia.org/wiki/Quicksort
[merge sort]: https://en.wikipedia.org/wiki/Merge_sort
[heap sort]: https://en.wikipedia.org/wiki/Heapsort
[introsort]: https://en.wikipedia.org/wiki/Introsort
[Timsort]: https://en.wikipedia.org/wiki/Timsort

[integer sorting]: https://en.wikipedia.org/wiki/Integer_sorting
[counting sort]: https://en.wikipedia.org/wiki/Counting_sort
[bucket sort]: https://en.wikipedia.org/wiki/Bucket_sort
[radix sort]: https://en.wikipedia.org/wiki/Radix_sort

[sorting animations]: https://www.toptal.com/developers/sorting-algorithms/
[interactive sorting animations]: https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html
[The Sound of Sorting]: http://panthema.net/2013/sound-of-sorting/

[Sorting Out Sorting]: https://www.youtube.com/watch?v=SJwEwA5gOkM
[sorting algorithm videos]: https://www.youtube.com/user/TutorialsCC/videos
[Timsort video]: https://www.youtube.com/watch?v=Nfi0BXmhbDw

[3 sorting algorithms]: https://www.youtube.com/watch?v=jHPexHsDxwQ
[9 sorting algorithms]: https://www.youtube.com/watch?v=ZZuD6iUe3Pc
[15 sorting algorithms]: https://www.youtube.com/watch?v=kPRA0W1kECg
[23 sorting algorithms]: https://www.youtube.com/watch?v=rqI6KT6cOas

[sorting algorithms with folk dances]: https://www.youtube.com/playlist?list=PLOmdoKois7_FK-ySGwHBkltzB11snW7KQ
[merge sort with German folk dance]: https://www.youtube.com/watch?v=dENca26N6V4
[quick sort with Hungarian folk dance]: https://www.youtube.com/watch?v=3San3uKKHgg

[sorting algorithms]: http://make.sc/oa-sorting-algorithms
