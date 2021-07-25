import pytest
from selenium import webdriver
@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
    elif browser=='firefox':
        driver=webdriver.Chrome()
    else:
        driver=webdriver.Ie
    return driver






def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')

def pytest_configure(config):
    config._metadata['project Name']='nop commerce'
    config._metadata['module Name']='customer'
    config._metadata['tester Name']='jaffar'
