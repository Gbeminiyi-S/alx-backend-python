#!/usr/bin/env python3
""" This module tests the utils package """

from parameterized import parameterized
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case class for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), 2),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nestedMap, path, expectedResult):
        """
        Test the access_nested_map function with different input scenarios.
        """
        self.assertEqual(access_nested_map(nestedMap, path), expectedResult)
