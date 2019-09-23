import pytest

#pytest needs to be installed using 'pip3 install pytest' command on terminal
#we run this program using py.test within pytestpackage where it resides
#to see print messages and more details run with command: py.test -v -s (-v is for verbose and -s is for printing the print statements)

#specifying setUp funciton to be a fixture will allow it to be executed before every test case method
@pytest.fixture()
def setUp():
    print("Will run once before every method")

#attaching fixture method by passing it as param in the method will allow it to be executed before the method
def test_methodA(setUp):
    print("Running method A")

def test_methodB(setUp):
    print("Running method B")

