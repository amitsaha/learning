from testinfra.modules import Package, SystemInfo
from behave import *

@given('we are on Linux')
def step_impl(context):
    #assert SystemInfo.type == 'linux'
    pass

@then('git should be installed')
def step_impl(context):
    git = Package('git')
    assert git.is_installed
