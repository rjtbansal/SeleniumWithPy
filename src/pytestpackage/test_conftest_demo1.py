import pytest

#pass fixtures method names as arguments to invoke setup and teardown methods
def test_demo1_methodA(oneTimeSetUp, setUp):
    print("Running conftest demo1 method A")

def test_demo1_methodB(oneTimeSetUp, setUp):
    print("Running conftest demo1 method B")