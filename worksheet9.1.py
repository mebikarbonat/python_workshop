#Muhammad Azizi Mohd Ariffin
#mazizi@fskm.uitm.edu.my

import requests

coordinate = {'0':['3.070149','101.504400'], '1':['3.066177', '101.527538'],
              '2':['2.970726', '101.714609']}

count = 1
for co in coordinate :
    lat = coordinate[co][0]
    lon = coordinate[co][1]
    url = 'https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=' + lat + '&lon=' + lon
    try :
        response = requests.get(url)
        data = response.json()
        print('The address of the coordinate ' + str(count))
        print(str(data['address']) + '\n')
    except :
        print('API Error')
    count += 1
    
    