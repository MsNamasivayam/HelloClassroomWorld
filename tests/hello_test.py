import unittest

from hello import *

class TestHello(unittest.TestCase):

    def test_say_hello(self):
        """Tests the hello output"""
        self.assertEqual(say_hello(), "Hello Classroom!")