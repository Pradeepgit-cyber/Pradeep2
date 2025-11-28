#Any pytest file should start with test_ or end with test_
# pytest method names should start wit test
# Any code should be wrapped in method only
# Method name should have sense
# -k stands for methid name execution, -s stand for logs in output, -v stands for more info metadata
# you can run specific file with py.test <file name>
# you can mark (tag) tests @pytest.mark.smoke and then run with -m
# you can skip tests with @pytest.mark.skip
# fixtures are used as setup and tear down methods for test cases - conftest file to generalize fixture and make it available to all test cases.
# datadriven and parameterization can be done with return statements in tuple format
# when you define fixture scope to class only, it will run once before class is initiated and at the end

import pytest

@pytest.fixture()
def setup():
    print("I will execute steps first")
    yield
    print("I will execute steps in last")

def test_fixtureDemo(setup):
    print("i will execute steps in fixture demo")


def test_firstProgram1():
    msg = "Hello first program"
    assert  msg == "hello", "Test failed because strings do not match"

@pytest.mark.smoke
@pytest.mark.xfail
def test_secondaryProgram2():
    a = 3
    b = 5
    assert a+2 == 6, "Addition failed"

@pytest.mark.skip
def test_secondaryProgram3():
    a = 2
    b = 3
    assert a+b == 5, "Addition passed"