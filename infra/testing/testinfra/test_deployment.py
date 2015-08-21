"""
Test service is deployed and running
"""

def test_httpd_is_running(Service):
    httpd = Service('httpd')
    assert httpd.is_enabled
    assert httpd.is_running

def test_httpd_is_serving(Command):
    assert Command('curl 127.0.0.1').rc == 0

