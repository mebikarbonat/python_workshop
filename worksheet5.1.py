#Muhammad Azizi Mohd Ariffin
#mazizi@fskm.uitm.edu.my

try :
    file = open(r'bmi.csv', 'r')
except :
    file = open(r'bmi.csv', 'w')
    file.write('name,heigh,weight,bmi \n')
    file.close()
    file = open(r'bmi.csv', 'r')

lineCount = 0
lines = file.readlines()
for line in lines :
    if lineCount == 0 :
        print('Usage History')
        print('Name | Height | Weight | BMI \n')
    else :
        print(line)
    lineCount += 1
file.close()
file = open(r'bmi.csv', 'a')

print('Hi, This program will calculate your bmi \n')
name = input('plase enter your name: ')
weight = int(input('please enter your weight(kg): '))
height = float(input('please enter your height(m): '))

bmi = round(weight / (height * height), 1)

print('Your BMI is ' + str(bmi))
if bmi < 18.5 :
    print('You are underweight')
elif bmi >= 18.5 and bmi < 25.0 :
    print('Your weight is desirable')
elif bmi >= 25.0 and bmi < 30: 
    print('You are overweight')
else :
    print('You are obese')
write = name + ',' + str(height) + ',' + str(weight) + ',' + str(bmi) + '\n'
file.write(write)
file.close