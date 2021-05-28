#Muhammad Azizi Mohd Ariffin
#mazizi@fskm.uitm.edu.my

print('Hi, This program will calculate your bmi \n')
weight = int(input('please enter your weight(kg): '))
height = float(input('please enter your height(m): '))

bmi = round(weight / (height * height), 0)

print('Your BMI is :' + str(bmi))