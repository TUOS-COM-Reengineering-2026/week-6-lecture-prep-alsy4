import unittest
from prep import strange_function

class MyTestCase(unittest.TestCase):
    def test_strange_function1(self):
        self.assertEqual(
            first=strange_function(1, 2, 3, 4),
            second='behaviour 3'
        )

        self.assertEqual(
            first=strange_function(1, 1, 2, 3),
            second='behaviour 1'
        )

        self.assertEqual(
            first=strange_function(1, 1, 3, 2),
            second='behaviour 2'
        )

        self.assertEqual(
            first=strange_function(1,2,1,1),
            second='behaviour 4'
        )

        self.assertEqual(
            first=strange_function(4,2,2,3),
            second='behaviour 5'
        )




    # TODO: Can you write more test cases below to increase the test coverage of `strange_function`?