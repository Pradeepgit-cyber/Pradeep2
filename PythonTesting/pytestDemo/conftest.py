import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will execute first")
    yield
    print("I will be executed last")

@pytest.fixture
def dataLoad():
    print("user profile data is being loaded")
    return ["Pradeep", "Test", "This is for testing"]

@pytest.fixture(params=[("chrome", "Pradeep"), "firefox", "opera", "edge"])
def crossBrowser(request):
    return request.param


