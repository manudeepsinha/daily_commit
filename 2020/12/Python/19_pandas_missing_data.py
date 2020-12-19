import numpy as np
 
# dictionary of lists
dict = {'First Sem Marks':[80,60,np.nan,91],
        'Second Sem Marks': [30, 45, 56, np.nan],
        'Third Sem Marks':[np.nan, 40, 80, 98]}
 
# creating a dataframe from list
df = pd.DataFrame(dict)
 
# using isnull() function to get boolean output, True for null vals, False for not null
df.isnull()



#Below is another code to fill null values

import numpy as np
 
# dictionary of lists
dict = {'First Sem Marks':[80,60,np.nan,91],
        'Second Sem Marks': [30, 45, 56, np.nan],
        'Third Sem Marks':[np.nan, 40, 80, 98]}
 
# creating a dataframe from dictionary
df = pd.DataFrame(dict)
 
# using fillna() for missing values  
df.fillna('Absent')



#Below is another code to drop rows and columns that contain null vals

import numpy as np
 
# dictionary of lists
dict = {'First Sem Marks':[80,60,np.nan,91],
        'Second Sem Marks': [30, 45, 56, np.nan],
        'Third Sem Marks':[np.nan, 40, 80, 98],
       'Fourth Sem Marks':[24,42,67,92]}
 
# creating a dataframe from dictionary
df = pd.DataFrame(dict)
 
# using drop() for missing values  
df.dropna()

