//Muhammad Azizi Mohd Ariffin
//mazizi@fskm.uitm.edu.my

import platform

def printOutPlatform():
    print("Hey I'm in the function code block")
    print("Your Computer Platform Type is :" + str(platform.platform()))
a = 1  
while True :
    print("Hey I'm in the while statement code block")
    
    if a == 1 :
        print("Hey I'm in the if statement code block")
        printOutPlatform()
    
    break
