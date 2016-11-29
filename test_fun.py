from unittest import TestCase
from tests import fun

class TestFun(TestCase):
    def test_fun(self):
        self.assertEqual(fun(1), 2)
