#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function."""

    def test_empty_list(self):
        """An empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_ordered_list(self):
        """The max value is returned from an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """The max value is returned from an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """The max value is returned from negative numbers."""
        self.assertEqual(max_integer([-1, -3, -2]), -1)

    def test_single_number(self):
        """A single-item list returns that item."""
        self.assertEqual(max_integer([9]), 9)

    def test_max_at_beginning(self):
        """The max value can be at the beginning."""
        self.assertEqual(max_integer([7, 3, 1]), 7)

    def test_duplicate_max(self):
        """Duplicate max values still return the max."""
        self.assertEqual(max_integer([1, 7, 7, 3]), 7)

    def test_float_values(self):
        """Float values can be compared."""
        self.assertEqual(max_integer([1.5, 3.2, 2.8]), 3.2)

    def test_string_values(self):
        """String values can be compared."""
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_invalid_non_iterable(self):
        """A non-iterable argument raises TypeError."""
        self.assertRaises(TypeError, max_integer, True)


if __name__ == '__main__':
    unittest.main()
