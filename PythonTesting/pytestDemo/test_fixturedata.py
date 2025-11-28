import pytest


@pytest.mark.usefixtures("dataLoad")
class TestExample2:
    def test_editProfile(self, dataLoad):
        # print(dataLoad)         #will print all the data
       print(dataLoad[0])         #will print data individually
       print(dataLoad[2])         #will print data individually
