#Muhammad Azizi Mohd Ariffin
#mazizi@fskm.uitm.edu.my

#This code will try to convert a string to int which will cause an error
text = 'Hi this will fail'

try :
    #this will cause error
    text = int(text)
except :
    print('Looks like you have failed to convert string to int type')