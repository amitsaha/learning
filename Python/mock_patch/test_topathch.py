from mock import patch

@patch('topatch.afunction')
class TestToPatch():
    
    def test_afunction(self, mock_afunction):
        mock_afunction('foo', 'bar')
        mock_afunction.assert_any_call('foo', 'bar')
