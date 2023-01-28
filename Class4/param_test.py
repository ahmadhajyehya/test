from unittest import TestCase

num_list = [1, 2, 3]


class NumberTest(TestCase):
    def test_numbers(self):
        for num in num_list:
            assert num > 0
