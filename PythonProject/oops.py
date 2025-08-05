# self keyword is mandatory for calling variable name into method.
# constructor name should be __init__
# can create multiple object for a single class

class Calculator:
    num = 100  # call it's as a variable/attributes

    def __init__(self, a, b):      #default constructor. It is used to initialize a new created object.
        self.firstnumber = a       #saves the first number to the object.
        self.secondnumber = b      #saves the second number.
        print('Called by a Constructor')  #The print line just shows a message to tell you the constructor ran.

    def getData(self):   #Method or Function
        print('I am executing a method for a class')   #when successfully called , its prints the message

    def Summation(self):
        return self.firstnumber + self.secondnumber + self.num  #method that calls the total summation

obj = Calculator(2,3)   #creates an object named obj from the Calculator class,Syntax to create an object in python
obj.getData()  #Calls the method getData() for the object obj. Output will be line 14
print(obj.Summation()) #calls summation method.


obj1 = Calculator(4,5)   #Syntax to create an object in python
obj1.getData()
print(obj1.Summation())
