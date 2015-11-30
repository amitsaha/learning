import unittest
from nose_parameterized import parameterized, param

@parameterized([param(2), param(3)])
def test_square(x):
    assert x**2 == x**2


class AddTestCase(unittest.TestCase):
    @parameterized.expand([
        ("string1", "string1"),
        ("string2", "string2")
    ])
    def test_check_string(self, _, s):
        assert isinstance(s, str)
