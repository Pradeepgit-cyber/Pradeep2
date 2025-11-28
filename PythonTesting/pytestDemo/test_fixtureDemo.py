import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo1(self):
        print("I will execute steps in fixture1 demo")

    def test_fixtureDemo2(self):
        print("I will execute steps in fixture2 demo")

    def test_fixtureDemo3(self):
        print("I will execute steps in fixture3 demo")

    def test_fixtureDemo4(self):
        print("I will execute steps in fixture4 demo")



