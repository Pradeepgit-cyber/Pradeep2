import self

from oops import Calculator


class childinheritance(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 3)


    def getcompletedata(self):
        return self.num2 + self.num + self.Summation()


obj = childinheritance()
print(obj.getcompletedata())


# test= Calculator(1,2)
# test.getData()
# print(test.Summation())
# print()