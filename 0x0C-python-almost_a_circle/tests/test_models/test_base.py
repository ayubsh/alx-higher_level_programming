#!/usr/bin/python3
"""Unittest for the base class """
import unittest
from models.base import Base

class TestBase_init(unittest.TestCase):
    """ testing the base class instances """
    def test_base_id(self):
        base1 = Base()
        self.assertEqual(base1.id, 1)

    def test_none_id(self):
        base_none = Base(None)
        self.assertEqual(base_none.id, 2)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_passed_id(self):
        base1 = Base(12)
        self.assertEqual(base1.id, 12)

    def test_one_passed_id(self):
        base1 = Base(99)
        base2 = Base()
        b = base1.id + base2.id
        self.assertEqual(b, 102)

    def test_str_id(self):
        base_str = Base("1")
        self.assertEqual(base_str.id, "1")

    def test_nb_inst(self):
        base1 = Base(5)
        with self.assertRaises(AttributeError):
            print(base1.__nb__instances)
    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)
if __name__ == "__main__":
    unittest.main()
