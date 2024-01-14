#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
from random import randrange
from contextlib import redirect_stdout
import io

def test_D_instantiation(self):
        '''Tests instantiation.'''
        re = Square(10)
        self.assertEqual(str(type(re)), "<class 'models.square.Square'>")
        self.assertTrue(isinstance(re, Base))
        d = {'_Rectangle__height': 10, '_Rectangle__width': 10,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(re.__dict__, d)

        with self.assertRaises(TypeError) as e:
            re = Square("1")
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            re = Square(1, "2")
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            re = Square(1, 2, "3")
        msg = "y must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            re = Square(-1)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)
