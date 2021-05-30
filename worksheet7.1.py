#Muhammad Azizi Mohd Ariffin
#mazizi@fskm.uitm.edu.my

def calculateCircleArea(r) :
    area = 3.14 * (r ** 2)
    return area
def goodbye() :
    print ("Goodbye..end of program")

radiusList = [43,64,5,4,3,10]
for r in radiusList:
    temp = calculateCircleArea(r)
    temp = round(temp, 2)
    print('The Circle Area with radius ' + str(r) + ': ' + str(temp))
goodbye()