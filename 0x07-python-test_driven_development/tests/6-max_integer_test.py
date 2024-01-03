#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_module_documentation(self):
        moddoc = __import__("6-max_integer").__doc__
        self.assertTrue(len(moddoc) > 1)

    def test_func_documentation(self):
        funcdoc = __import__("6-max_integer").max_integer.__doc__
        self.assertTrue(len(funcdoc) > 1)

    def test_empt_list(self):
        self.assertIsNone(max_integer([]))

    def test_max_begining(self):
        self.assertEqual(max_integer([100, 20, 10, 40]), 100)

    def test_max_end(self):
        self.assertEqual(max_integer([40, 20, 30, 100]), 100)

    def test_max_middle(self):
        self.assertEqual(max_integer([40, 10, 100, 20]), 100)

    def test_max_one_negative(self):
        self.assertEqual(max_integer([10, -50, 100, 40]), 100)

    def test_one_element(self):
        self.assertEqual(max_integer([10]), 10)

    def test_negative(self):
        self.assertEqual(max_integer([-5, -100, -10, -60]), -5)


if __name__ == "__main__":
    unittest.main()
