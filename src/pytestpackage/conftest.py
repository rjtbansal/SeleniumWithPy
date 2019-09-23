import pytest

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")

#scope with value as module ensures that below method will run once in the beginning and the end and not for every test case method
@pytest.yield_fixture(scope="module")
def oneTimeSetUp():
    print("Running conftest demo one time setUp")
    yield
    print("Running conftest demo one time tearDown")