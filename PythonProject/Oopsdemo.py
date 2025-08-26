#self is mandatory for calling variables name into methods


class Calculator:
    num = 300    #class variable or attributes

    def __init__(self,a,b):  #default constructor. It is used to initialize a new created object.
        self.firstnumber = a
        self.secondnumber = b
        print('I am executing a constructor')

    def getData(self):
        print('I am executing a method for a class')

    def summation(self):
        return self.firstnumber + self.secondnumber + self.num

obj = Calculator(2,3)  #syntax to create objects in python
obj.getData()
print(obj.summation())

obj1 = Calculator(4,5)  #syntax to create objects in python
obj1.getData()
print(obj1.summation())