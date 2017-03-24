#!python

from palindromes import is_palindrome
import unittest


class TestPalindromes(unittest.TestCase):

    def test_is_palindrome_with_mirrored_strings(self):
        # simple palindromes that are mirrored strings
        assert is_palindrome('') is True  # base case
        assert is_palindrome('A') is True  # base case
        assert is_palindrome('BB') is True
        assert is_palindrome('LOL') is True
        assert is_palindrome('noon') is True
        assert is_palindrome('radar') is True
        assert is_palindrome('racecar') is True

    # Enable each of these test cases by deleting DISABLED_
    def DISABLED_test_is_palindrome_with_mixed_casing(self):
        # palindromes with mixed leter casing
        assert is_palindrome('Bb') is True
        assert is_palindrome('NoOn') is True
        assert is_palindrome('Radar') is True
        assert is_palindrome('RaceCar') is True

    def DISABLED_test_is_palindrome_with_whitespace(self):
        # palindromes with whitespace
        assert is_palindrome('taco cat') is True
        assert is_palindrome('race car') is True
        assert is_palindrome('race fast safe car') is True

    def DISABLED_test_is_palindrome_with_whitespace_and_mixed_casing(self):
        # palindromes with whitespace and mixed letter casing
        assert is_palindrome('Taco Cat') is True
        assert is_palindrome('Race Car') is True
        assert is_palindrome('Race Fast Safe Car') is True

    def DISABLED_test_is_palindrome_with_whitespace_and_punctuation(self):
        # palindromes with whitespace and punctuation
        assert is_palindrome('taco cat!') is True
        assert is_palindrome('race, car!!') is True
        assert is_palindrome('race fast, safe car.') is True

    def DISABLED_test_is_palindrome_with_mixed_casing_and_punctuation(self):
        # palindromes with whitespace, punctuation and mixed letter casing
        assert is_palindrome('Race fast, safe car.') is True
        assert is_palindrome('Was it a car or a cat I saw?') is True
        assert is_palindrome("Go hang a salami, I'm a lasagna hog.") is True
        assert is_palindrome('A man, a plan, a canal - Panama!') is True

    def test_is_palindrome_with_non_palindromic_strings(self):
        assert is_palindrome('AB') is False  # even length
        assert is_palindrome('ABC') is False  # odd length
        assert is_palindrome('doge') is False
        assert is_palindrome('monkey') is False
        assert is_palindrome('chicken, monkey!') is False


if __name__ == '__main__':
    unittest.main()
