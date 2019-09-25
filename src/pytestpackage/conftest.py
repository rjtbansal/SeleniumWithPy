import pytest


@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")

#scope with value as module ensures that below method will run once in the beginning and the end and not for every test case method
@pytest.yield_fixture(scope="module")

#below we want browser and osType params to be passed through command line
def oneTimeSetUp(browser, osType):
    print("Running conftest demo one time setUp")
    browser = browser.lower() if browser is not None else browser
    if browser == "firefox":
        print("Running tests on Firefox")
    else:
        print("Running tests on Chrome")
    if osType=="MacOS":
        print("MacOS instance created")
    else:
        print("Windows instance created")
    yield
    print("Running conftest demo one time tearDown")

def pytest_addoption(parser):
    #adding browser and osType as a command line option using pytest parser arg
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of OS")

#for browser to be accepted from commandline we need to map it to fixture function below
#scope will be session as its session based

@pytest.fixture(scope="session")
def browser(request):
    #we pass request param
    #getting option --browser value
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")




