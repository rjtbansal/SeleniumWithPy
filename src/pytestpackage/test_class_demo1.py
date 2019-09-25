import pytest
from pytestpackage.class_to_test import SomeClassToTest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestClassDemo():
    #setting autouse to true will apply above fixtures to all methods
    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.test_instance = SomeClassToTest(10)

    def test_methodA(self):
        result = self.test_instance.sumNumbers(2,8)
        assert result == 20
        print("Running method A")

    def test_methodB(self):
        print("Running method B")


