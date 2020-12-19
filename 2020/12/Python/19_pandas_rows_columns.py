#To print a specific column:
import pandas as pd

#reading data from csv file that has been uploaded in github: https://github.com/manudeepsinha/daily_code/blob/main/2020/12/Python/13_sem_marks.csv
data = pd.read_csv('sem_marks.csv')

df = pd.DataFrame(data)

#printing names and semester columns only
#to print only one column, use single pair of [] as print(df['Name'])
print(df[['Name','Sem']])


#Following is another code for rows:

import pandas as pd

data = pd.read_csv('sem_marks.csv')

#retriving row by loc method
first = data.loc[0]
second = data.loc[1]

#head() prints the first five enteries of a given data frame
#can also print n number, where passing n in head()
print('First five enteries are: \n',data.head())

print('\n\n')

print('First two entries are:')

#printing first and second enteries only
print(first,'\n'*2,second)

print('\n\n')

#printing iloc[] and passing single integer to fetch that perticular row
row3 = data.iloc[2]

print('Third entry is:')

print(row3)