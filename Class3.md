### Class 3: Friday, March 24 – String Algorithms

**Topics:**
- [unit testing], Python's [`unittest` module] and [`pytest` tool]
- [palindromes]: strings that read the same forwards and backwards, ignoring punctuation, whitespace, and letter casing
- [string searching]: find the starting index of the first occurrence of a pattern in a string
- [permutation]: arrangement of all items in a set into a sequence or order
- [anagrams]: permutations of words or phrases that produce another word

**Resources:**
- read StackOverflow's answers to the question [what is unit testing?]
- read The Hitchhiker's Guide to Python's tutorial on [testing your code]
- play around with Wordsmith's [Internet Anagram Server]

**Challenges:**
- implement palindrome checking functions using [palindromes starter code]:
    - implement `is_palindrome_iterative` - iterative version
    - implement `is_palindrome_recursive` - recursive version
    - run `python palindromes.py string1 string2 ... stringN` to test `is_palindrome`
        - example: `python palindromes.py ABC noon RaceCar 'Taco, Cat'` gives the result:
        > `FAIL: 'ABC' is not a palindrome`<br/>
        > `PASS: 'noon' is a palindrome`<br/>
        > `PASS: 'RaceCar' is a palindrome`<br/>
        > `PASS: 'Taco, Cat' is a palindrome`<br/>
    - run `pytest test_palindromes.py` to run the [palindromes unit tests] and fix any failures
- implement string searching functions (try both iterative and recursive versions):
    - implement `find(string, pattern)` - true if `string` contains the entire `pattern`
    - implement `find_index(string, pattern)` - the starting index of the first occurrence of `pattern` in `string`
    - *stretch:* implement `find_all_indexes(string, pattern)` - a list of the starting indexes of all occurrences of `pattern` in `string`
- write your own unit tests for your string searching functions
    - include several test cases that are both positive (examples) and negative (counterexamples)
- annotate functions with complexity analysis

**Stretch Challenges:**
- implement permutation generating functions (try both iterative and recursive versions)
- implement anagram generating functions (try both iterative and recursive versions)
    - *Hint:* use the Unix words list located at: `/usr/share/dict/words`

**Project:**
- [phone call routing] scenarios 1 and 2:
    - implement phone number prefix matching
- annotate functions with complexity analysis

[unit testing]: https://en.wikipedia.org/wiki/Unit_testing
[`unittest` module]: https://docs.python.org/2/library/unittest.html
[`pytest` tool]: http://docs.pytest.org/en/latest/
[what is unit testing?]: http://stackoverflow.com/questions/1383/what-is-unit-testing
[testing your code]: http://docs.python-guide.org/en/latest/writing/tests/

[string searching]: https://en.wikipedia.org/wiki/String_searching_algorithm
[palindromes]: https://en.wikipedia.org/wiki/Palindrome
[permutation]: https://en.wikipedia.org/wiki/Permutation
[anagrams]: https://en.wikipedia.org/wiki/Anagram
[Internet Anagram Server]: http://www.wordsmith.org/anagram/

[palindromes starter code]: source/palindromes.py
[palindromes unit tests]: source/test_palindromes.py

[phone call routing]: http://make.sc/db-phone-call-routing
