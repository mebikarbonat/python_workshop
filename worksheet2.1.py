#Muhammad Azizi Mohd Ariffin
#mazizi@fskm.uitm.edu.my

thisIsInteger = 10
thisIsFloat = 45.6
thisIsString = "Hello, this program demonstrate variable"
thisIsList = ["Camelia", "Hibiscus", "Rose"]

print('The data type is: ' + str(type(thisIsInteger)))
thisIsInteger = float(thisIsInteger)
print('Converting the integer data to float :' + str(type(thisIsInteger)))

print('The data type is: ' + str(type(thisIsFloat)))
thisIsFloat = int(thisIsFloat)
print('Converting the float data to integer :' + str(type(thisIsFloat)))

print('The data type is: ' + str(type(thisIsString)))
print('This data cannot be converted to string but we can know it length')
print('The data length is ' + str(len(thisIsString)))

print('The data type is: ' + str(type(thisIsList)))
print('This data cannot be converted to other but we can know it length')
print('The data length is ' + str(len(thisIsList)))