### Class 2: Wednesday, March 22 – Recursion & Search Algorithms

**Topics:**
- compare [iteration] and [recursion] with [factorial] function
- searching algorithms: [linear search] and [binary search]

**Resources:**
- review Make School's [algorithm analysis slides]
- read InterviewCake's [article on the idea behind big O notation][IC big O]
- read StackOverflow's [plain English explanations of big O notation][SO big O]

**Challenges:**
- implement iterative [factorial] function using [recursion starter code]:
    - implement `factorial(n)` - the product of the integers 1 through *n*
    - run `python recursion.py number` to test `factorial` on a number
        - example: `python recursion.py 8` gives the result `factorial(8) => 40320`
    - run `pytest test_recursion.py` to run the [recursion unit tests] and fix any failures
- implement recursive linear and binary search algorithms using [search starter code]:
    - implement `linear_search(array, item)` - the first index of `item` in `array`
    - implement `binary_search(array, item)` - the index of `item` in sorted `array`
    - run `pytest test_search.py` to run the [search unit tests] and fix any failures
- annotate all functions with running time complexity analysis

**Stretch Challenges:**
- implement efficient [permutation] and [combination] functions

[iteration]: https://en.wikipedia.org/wiki/Iteration
[recursion]: https://en.wikipedia.org/wiki/Recursion_(computer_science)
[factorial]: https://en.wikipedia.org/wiki/Factorial
[linear search]: https://en.wikipedia.org/wiki/Linear_search
[binary search]: https://en.wikipedia.org/wiki/Binary_search_algorithm
[permutation]: https://en.wikipedia.org/wiki/Permutation
[combination]: https://en.wikipedia.org/wiki/Combination

[algorithm analysis slides]: slides/AlgorithmAnalysis.pdf
[IC big O]: https://www.interviewcake.com/article/python/big-o-notation-time-and-space-complexity
[SO big O]: http://stackoverflow.com/questions/487258/what-is-a-plain-english-explanation-of-big-o-notation

[recursion starter code]: source/recursion.py
[recursion unit tests]: source/test_recursion.py
[search starter code]: source/search.py
[search unit tests]: source/test_search.py
