from PythonProject.Oopsdemo import Calculator


class ChildImp(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 12, 10)

    def getData(self):
        return self.num2 + self.num + self.summation()


obj = ChildImp()
print(obj.getData())