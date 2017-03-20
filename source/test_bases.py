#!python

from bases import decode, encode, convert
import unittest


class BasesTest(unittest.TestCase):

    def test_decode(self):
        assert decode('10', 2) == 2
        assert decode('10', 3) == 3
        assert decode('10', 4) == 4
        assert decode('10', 5) == 5
        assert decode('10', 8) == 8
        assert decode('10', 10) == 10
        assert decode('10', 16) == 16
        assert decode('10', 32) == 32

        assert decode('101', 2) == 5
        assert decode('101', 3) == 10
        assert decode('101', 4) == 17
        assert decode('101', 5) == 26
        assert decode('101', 8) == 65
        assert decode('101', 10) == 101
        assert decode('101', 16) == 257
        assert decode('101', 32) == 1025

        assert decode('111', 2) == 7
        assert decode('121', 3) == 16
        assert decode('123', 4) == 27
        assert decode('234', 5) == 69
        assert decode('246', 8) == 166
        assert decode('864', 10) == 864
        assert decode('cab', 16) == 3243
        assert decode('cat', 32) == 12637

    def test_encode(self):
        assert encode(10, 2) == '1010'
        assert encode(10, 3) == '101'
        assert encode(10, 4) == '22'
        assert encode(10, 5) == '20'
        assert encode(10, 8) == '12'
        assert encode(10, 10) == '10'
        assert encode(10, 16) == 'a'
        assert encode(10, 32) == 'a'

        assert encode(100, 2) == '1100100'
        assert encode(100, 3) == '10201'
        assert encode(100, 4) == '1210'
        assert encode(100, 5) == '400'
        assert encode(100, 8) == '144'
        assert encode(100, 10) == '100'
        assert encode(100, 16) == '64'
        assert encode(100, 32) == '34'

        assert encode(1234, 2) == '10011010010'
        assert encode(1234, 3) == '1200201'
        assert encode(1234, 4) == '103102'
        assert encode(1234, 5) == '14414'
        assert encode(1234, 8) == '2322'
        assert encode(1234, 10) == '1234'
        assert encode(1234, 16) == '4d2'
        assert encode(1234, 32) == '16i'

    def test_convert(self):
        assert convert('1010', 2, 3) == '101'
        assert convert('1010', 2, 4) == '22'
        assert convert('1010', 2, 8) == '12'
        assert convert('1010', 2, 10) == '10'

        assert convert('101', 3, 2) == '1010'
        assert convert('22', 4, 2) == '1010'
        assert convert('12', 8, 2) == '1010'
        assert convert('10', 10, 2) == '1010'

        assert convert('77', 8, 2) == '111111'
        assert convert('77', 8, 4) == '333'
        assert convert('77', 8, 10) == '63'
        assert convert('77', 8, 16) == '3f'

        assert convert('ff', 16, 2) == '11111111'
        assert convert('ff', 16, 4) == '3333'
        assert convert('ff', 16, 8) == '377'
        assert convert('ff', 16, 10) == '255'


if __name__ == '__main__':
    unittest.main()
