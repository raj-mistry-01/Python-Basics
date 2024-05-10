# attribute means the variables of the class.
# normal Variable Vs Class Attribute.

vaR = 10 # a normal variable
print(vaR) # will not generate any error.

# vaR can be accessed through out the programme.

class attribute_ :
    pass

vaRcreator = attribute_() # created an onject of the class attribute_()
vaRcreator.value = 110 # this .value will be called as the attribute of the object.
# value is a also variable but not normal , an object variable (means attribute.) 
#print(value) will lead to an error.
print(vaRcreator.value)
print(type(vaRcreator)) # will give <class "__main__.attribute_"> it is a object
print(vaRcreator.value) # will give <class "int"> it is a atribute.