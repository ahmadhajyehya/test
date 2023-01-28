import unittest

class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('hello')

    def test_01(self):
        assert 1 > 0

    @classmethod
    def tearDownClass(self):
        print('bye')
