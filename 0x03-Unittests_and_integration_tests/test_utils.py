#!/usr/bin/env python3

"""
Testcase, to test utils.access_nested_map
"""

import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any


class TestAccesNestedMap(unittest.TestCase):
    """
    Test the access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, output: Any) -> None:
        """
        Tested if the access_nested_map produces the correct
        output
        """
        self.assertEqual(access_nested_map(nested_map, path), output)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_acces_mested_map_exception(self, nested_map: Mapping,
                                        path: Sequence) -> None:
        """
        test if the access_nested_map raise the correct exception
        with wrong input
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    tested if the get_json function returns the correct
    output
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch("requests.get")
    def test_get_json(self, test_url: str,
                      test_payload: Mapping,
                      mock_get: Mock) -> None:
        """
        tested if the get_json function returns the correct
        output
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        mock_get.return_value = mock_response

        self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """
    test the momoize function from the utils
    """
    def test_memoize(self) -> None:
        """
        test if the memoize works fine
        """
        class TestClass:
            """
            test class
            """
            def a_method(self) -> int:
                """
                test method
                """
                return 42

            @memoize
            def a_property(self) -> int:
                """
                test method
                """
                return self.a_method()

        with patch.object(TestClass, "a_method") as mock_method:
            obj = TestClass()
            obj.a_property()
            obj.a_property()
            mock_method.assert_called_once()
