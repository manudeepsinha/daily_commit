#importing pandas library
import pandas as pd

#list of items that we want in data frame
lst = ['my','name','is','m']

#calling DataFrame() function and passing lst as argument
df = pd.DataFrame(lst)

#printing data frame with 0 as column name
print(df)

#Following is another code to insert dictionary data in data frame.

#importing pandas library
import pandas as pd

#data present in dictionary that we want in data frame
data = { 'Roll num' : [1,2,3,4],
         'Name' : ['Abhay','Bhanu','Chintu','Daya']}

#calling DataFrame() function and passing data as argument creating DataFrame
df = pd.DataFrame(data)

#printing the data frame
print(df)