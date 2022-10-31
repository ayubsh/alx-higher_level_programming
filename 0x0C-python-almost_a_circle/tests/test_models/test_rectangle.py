#!/usr/bin/python3
""" Unittes for Rectangle """
import unittest
import io
import sys
from models.rectangle import Rectangle


class TestRecInit(unittest.TestCase):
    """ testing the initialization of rectangle class """
    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)


    def test_two_args(self):
        rec1 = Rectangle(10, 2)
        rec2 = Rectangle(2, 10)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, rec.width)

    def test_width_setter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.width = 10
        self.assertEqual(10, rec.width)

    def test_height_getter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, rec.height)

    def test_height_setter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.height = 10
        self.assertEqual(10, rec.height)

    def test_x_getter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, rec.x)

    def test_x_setter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.x = 10
        self.assertEqual(10, rec.x)

    def test_y_getter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, rec.y)

    def test_y_setter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.y = 10
        self.assertEqual(10, rec.y)

class TestRecArea(unittest.TestCase):
    """ test the area of the rectangle """
    def setUp(self):
        self.rec1 = Rectangle(3, 4, 0, 0, 0)
        self.rec3 = Rectangle(1000000000000000, 10000000000000, 0, 0, 0)
        self.rec4 = Rectangle(2, 3, 2, 2, 2)

    def test_normal_area(self):
        self.assertEqual(12, self.rec1.area())

    def test_large_area(self):
        self.assertEqual(10000000000000000000000000000, self.rec3.area())

    def test_new_att_area(self):
        self.rec4.width = 5
        self.rec4.height = 6
        self.assertEqual(30, self.rec4.area())
            
class TestRecDisplay(unittest.TestCase):
    """ tests displaying rectangle to stdout """
    def setUp(self):
        self.r1 = Rectangle(2, 3, 0, 0, 0)
        self.r2 = Rectangle(3, 2, 1, 0, 1)
        self.r3 = Rectangle(4, 5, 0, 1, 0)
        self.r4 = Rectangle(2, 4, 3, 2, 0)
        self.r5 = Rectangle(5, 1, 2, 4, 7)

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout.
        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_display_wh(self):
        capture = TestRecDisplay.capture_stdout(self.r1, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_whx(self):
        capture = TestRecDisplay.capture_stdout(self.r2, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def test_display_why(self):
        capture = TestRecDisplay.capture_stdout(self.r3, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_whxy(self):
        capture = TestRecDisplay.capture_stdout(self.r4, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        with self.assertRaises(TypeError):
            self.r5.display(1)

    def test_str_wh(self):
        r = Rectangle(4, 6)
        capture = TestRecDisplay.capture_stdout(r, "print")
        correct = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_whx(self):
        r = Rectangle(5, 5, 1)
        correct = "[Rectangle] ({}) 1/0 - 5/5".format(r.id)
        self.assertEqual(correct, r.__str__())

    def test_str_whxy(self):
        r = Rectangle(1, 8, 2, 4)
        correct = "[Rectangle] ({}) 2/4 - 1/8".format(r.id)
        self.assertEqual(correct, str(r))

    def test_str_whixy(self):
        r = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(r))

    def test_str_change_atr(self):
        r = Rectangle(7, 7, 0, 0, [4])
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))

    def test_str_arg1(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)

