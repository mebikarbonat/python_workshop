#Muhammad Azizi Mohd Ariffin
#mazizi@fskm.uitm.edu.my

import pandas as pd

def convertToFeet(m) :
    return( m * 3.281)

df = pd.read_csv('nile.csv')
print(df.head())

runConvert = df.apply(lambda row: convertToFeet(row['Flood']), axis=1)
df['feet'] = runConvert
print(df.head())
print('\n')
print('The mean of flood is ' + str(df['Flood'].mean()))
print('The median of flood is ' + str(df['Flood'].median()))
print('The mean of flood in feet is ' + str(df['feet'].mean()))
print('The median of flood in feet is ' + str(df['feet'].median()))

#storing the df to csv file
df.to_csv(r'nile_feet.csv', index=False)