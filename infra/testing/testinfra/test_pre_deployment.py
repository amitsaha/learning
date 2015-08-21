"""
pre-deployment tests
"""
def test_is_linux(SystemInfo):
    assert SystemInfo.type == 'linux'

def test_git_is_installed(Package):
    git = Package('git')
    assert git.is_installed

def test_mnt_test_code_is_mounted(File):
    mnt_test = File('/mnt/test')
    assert mnt_test.exists
