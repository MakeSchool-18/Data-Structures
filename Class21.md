### Class 21: Friday, May 12 – Memoization & Dynamic Programming

**Topics:**
- revisit [recursion] with [memoization] and [dynamic programming]
<!-- - [combinatorial optimization], [greedy algorithms] -->

**Resources:**
- play with VisuAlgo's [interactive recursion and memoization visualizations][visualgo recursion]
- read WikiBooks's Algorithms book chapter on [memoization and dynamic programming][wikibooks dp]
<!-- - read about [greedy algorithms][wikibooks greedy] on WikiBooks -->

**Challenges:**
- implement the following recursive functions with memoization and dynamic programming using [recursion starter code]:
    - [factorial] function
    - [fibonacci] function
    - [change-making problem] – solve [HackerRank's coin change problem]
- annotate functions with complexity analysis
- benchmark performance of plain recursion versus memoized recursion and dynamic programming
- run `pytest test_recursion.py` to run [recursion unit tests] and fix any failures

**Stretch Challenges:**
- implement [permutation] and [combination] functions
- implement `@memoized` [decorator] to memoize any recursive function

[combinatorial optimization]: https://en.wikipedia.org/wiki/Combinatorial_optimization
[greedy algorithms]: https://en.wikipedia.org/wiki/Greedy_algorithm

[recursion]: https://en.wikipedia.org/wiki/Recursion_(computer_science)
[memoization]: https://en.wikipedia.org/wiki/Memoization
[dynamic programming]: https://en.wikipedia.org/wiki/Dynamic_programming

[factorial]: https://en.wikipedia.org/wiki/Factorial
[fibonacci]: https://en.wikipedia.org/wiki/Fibonacci_number
[permutation]: https://en.wikipedia.org/wiki/Permutation
[combination]: https://en.wikipedia.org/wiki/Combination

[change-making problem]: https://en.wikipedia.org/wiki/Change-making_problem
[HackerRank's coin change problem]: https://www.hackerrank.com/challenges/coin-change
[decorator]: https://wiki.python.org/moin/PythonDecorators

[wikibooks greedy]: https://en.wikibooks.org/wiki/Algorithms/Greedy_Algorithms
[wikibooks dp]: https://en.wikibooks.org/wiki/Algorithms/Dynamic_Programming
[visualgo recursion]: https://visualgo.net/recursion

[recursion starter code]: source/recursion.py
[recursion unit tests]: source/test_recursion.py
