# Test for the role of PYTHONHASHSEED - urlllib urlencode

import urllib
urlencode_input = {'param1': 'value',
                   'param2': 'value'
                   }
expected_query_string = 'param1=value&param2=value'

# This will fail for *some* PYTHONHASHSEED
def test_urlencode_1():
    assert urllib.urlencode(urlencode_input) == expected_query_string

# This will not fail for *any* PYTHONHASHSEED
def test_urlencode_2():
    query_string = urllib.urlencode(urlencode_input)
    assert 'param1=value' in query_string
    assert 'param2=value' in query_string
