import mock

def ask_for_input():
    return input('Input something')
    
def test_input():
    with mock.patch('builtins.input', return_value='something'):
        assert ask_for_input() == 'something'
