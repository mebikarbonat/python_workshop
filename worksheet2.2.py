#Muhammad Azizi Mohd Ariffin
#mazizi@fskm.uitm.edu.my

statement = 'My name is ali and my age is 17 years old'
#getting only the age number from the string
age = statement[29:31]
print(type(age))
print('The age is ' + age)

#converting to the age to int
age = int(age)
print(type(age))
print('The age is ' + str(age))