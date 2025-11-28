#Any pytest file should start with test_ or end with test_
# pytest method names should start wit test
# Any code should be wrapped in method only
import pytest


def test_firtProgram():
    print("Hello")

@pytest.mark.smoke
def test_secondaryProgram2():
    print("Hello second program ")


def test_crossBrowser(crossBrowser):
    print(crossBrowser)
