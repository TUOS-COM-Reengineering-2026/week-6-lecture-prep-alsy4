import unittest
import lecture
from unittest.mock import patch

class MyTestCase(unittest.TestCase):

    @patch('lecture.randomised_function')
    def test_randomised_function(self, mock_randomised_function):
        mock_randomised_function.return_value = 'software'
        self.assertEqual('software', lecture.randomised_function())
