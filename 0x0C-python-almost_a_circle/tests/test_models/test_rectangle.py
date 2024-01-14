#!/usr/bin/python3
'''Module for Rectangle tests'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from random import randrange
from contextlib import redirect_stdout
import io

 def test_D_instantiation(self):
        re = Rectangle(10, 20)
        self.assertEqual(str(type(re)), "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(re, Base))
        d = {'_Rectangle__height': 20, '_Rectangle__width': 10,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
	with self.assertRaises(TypeError) as e:
            re = Rectangle(1, "2")
        msg = "height must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            re = Rectangle(1, 2, "3")
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            re = Rectangle(1, 2, 3, "4")
        msg = "y must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            re = Rectangle(-1, 2)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)
