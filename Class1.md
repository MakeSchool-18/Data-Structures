### Class 1: Monday, March 20 – Number Bases

**Topics:**
- number bases: [decimal], [binary], [hexadecimal]
- [negative integer representations]: signed magnitude, ones' complement, two's complement

**Resources:**
- review Make School's [slides on number bases][number bases slides]
- read BetterExplained's [article on number systems and bases][number bases article]
- play with Dan Wolff's live-updating [base conversion calculator]

**Challenges:**
- practice conversions on [number bases worksheet]
- implement base conversion functions for positive numbers using [starter code]:
    - implement `decode` - convert a number from any base to base 10
    - implement `encode` - convert a number from base 10 to any base
    - implement `convert` - convert a number from any base to any other base
    - run `python bases.py number base1 base2` to test `convert` on a number
        - example: `python bases.py 42 10 2` gives the result `101010`
    - run `pytest test_bases.py` to run the [unit tests] and fix any failures

**Stretch Challenges:**
- implement base conversion for negative binary numbers (using two's complement)
- implement base conversion for fractional numbers (using a [radix point])

[decimal]: https://en.wikipedia.org/wiki/Decimal
[binary]: https://en.wikipedia.org/wiki/Binary_number
[hexadecimal]: https://en.wikipedia.org/wiki/Hexadecimal
[negative integer representations]: https://en.wikipedia.org/wiki/Signed_number_representations
[radix point]: https://en.wikipedia.org/wiki/Radix_point

[number bases slides]: slides/NumberBases.pdf
[number bases worksheet]: slides/NumberBasesWorksheet.pdf
[number bases article]: https://betterexplained.com/articles/numbers-and-bases/
[base conversion calculator]: https://baseconvert.com/

[starter code]: source/bases.py
[unit tests]: source/test_bases.py
