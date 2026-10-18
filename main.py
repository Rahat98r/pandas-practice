import numpy as np
import pandas as pd
#1.Creating a dataframe from dictionery
data ={'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
dframe = pd.DataFrame(data)
print("DataFrame from dictionary :\n",dframe)

# #2.DataFrame with Specified Index Labels
# Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels.
# Sample DataFrame:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data,index= labels)

print("Data frame with specified index labels:\n",df)

# 3. DataFrame Basic Summary Information

# Write a Pandas program to display a summary of the basic information about a specified DataFrame and its data.
print(df.info())

#Select the first 3 rows of the datframe
print("First three rows of the DataFrame :\n",df.iloc[:3])