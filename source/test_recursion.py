#!python

from recursion import factorial, fibonacci
import unittest


class TestRecursion(unittest.TestCase):
    def test_factorial_with_small_integers(self):
        # factorial should return the product n*(n-1)*...*2*1 for n >= 0
        assert factorial(0) == 1  # base case
        assert factorial(1) == 1  # base case
        assert factorial(2) == 2*1
        assert factorial(3) == 3*2*1
        assert factorial(4) == 4*3*2*1
        assert factorial(5) == 5*4*3*2*1
        assert factorial(6) == 6*5*4*3*2*1
        assert factorial(7) == 7*6*5*4*3*2*1
        assert factorial(8) == 8*7*6*5*4*3*2*1
        assert factorial(9) == 9*8*7*6*5*4*3*2*1
        assert factorial(10) == 10*9*8*7*6*5*4*3*2*1

    def test_factorial_with_large_integers(self):
        assert factorial(15) == 1307674368000
        assert factorial(20) == 2432902008176640000
        assert factorial(25) == 15511210043330985984000000
        assert factorial(30) == 265252859812191058636308480000000

    def test_factorial_with_negative_integers(self):
        # factorial should raise a ValueError for n < 0
        with self.assertRaises(ValueError, msg='function undefined for n < 0'):
            factorial(-1)
            factorial(-5)

    def test_factorial_with_floating_point_numbers(self):
        # factorial should raise a ValueError for non-integer n
        with self.assertRaises(ValueError, msg='function undefined for float'):
            factorial(2.0)
            factorial(3.14159)

    def test_fibonacci_with_small_integers(self):
        # fibonacci should return fibonacci(n-1) + fibonacci(n-2) for n >= 0
        assert fibonacci(0) == 0  # base case
        assert fibonacci(1) == 1  # base case
        assert fibonacci(2) == 1
        assert fibonacci(3) == 2
        assert fibonacci(4) == 3
        assert fibonacci(5) == 5
        assert fibonacci(6) == 8
        assert fibonacci(7) == 13
        assert fibonacci(8) == 21
        assert fibonacci(9) == 34
        assert fibonacci(10) == 55

    def test_fibonacci_with_large_integers(self):
        # these could run for a long time...
        assert fibonacci(15) == 610
        assert fibonacci(20) == 6765
        assert fibonacci(25) == 75025
        # you may need to be very patient for these...
        # assert fibonacci(30) == 832040
        # assert fibonacci(35) == 9227465
        # assert fibonacci(40) == 102334155

    def test_fibonacci_with_negative_integers(self):
        # fibonacci should raise a ValueError for n < 0
        with self.assertRaises(ValueError, msg='function undefined for n < 0'):
            fibonacci(-1)
            fibonacci(-5)

    def test_fibonacci_with_floating_point_numbers(self):
        # fibonacci should raise a ValueError for non-integer n
        with self.assertRaises(ValueError, msg='function undefined for float'):
            fibonacci(2.0)
            fibonacci(3.14159)


if __name__ == '__main__':
    unittest.main()
