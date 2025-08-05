

values = [1, 2, 3, "Pradeep", 4.5]  #list data types. Can be multiple values.

print(values[1])  #output - 2
print(values[2]) #output - 3
print(values[-1]) #output - 4.5. -1 means last value/index of a list
print(values[1:3]) #output - 2, 3 . It means it will pick the range of any values/index
values.insert(4,"kumar") #to insert any values in between
values.append("End") #to insert any values in the end
values[3] = "PRADEEP" #updating values
del values[0]    #deleting any values in the list

print(values)


#Tuple - same as list data type but is not editable as List Data type

val = (1, 1, "Pradeep", 4.5)
print(val)


#Dictionary data types

dic = {"a" : 1, "b" : 2.5, "name" : "Pradeep"}
print(dic['b'])
print(dic["name"])


#how to create Dictinories from empty dictinory by adding key value pairs

dict = {}  #empty dictonary

dict["Firstname"] = "Pradeep"  #key values
dict["Secondname"] = "kumar"
dict["Lastname"] = 'Baraik'
dict["Gender"] = "Male"
print(dict)

print(dict["Gender"])