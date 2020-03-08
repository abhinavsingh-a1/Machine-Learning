import pandas as pd
import random
#https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
#https://www.analyticsvidhya.com/blog/2020/02/loc-iloc-pandas/

# DESCRIPTION
# loc is label-based, which means that we have to specify the name of the rows and columns that we need to filter out.
# On the other hand, iloc is integer index-based. So here, we have to specify rows and columns by their integer index.

# read the data from the downloaded CSV file.
data = pd.read_csv('https://s3-eu-west-1.amazonaws.com/shanebucket/downloads/uk-500.csv')
# set a numeric id for use as an index for examples.
data['id'] = [random.randint(0,1000) for x in range(data.shape[0])]
 
print(data.head(5))

# Single selections using iloc and DataFrame
# Rows:
print(data.iloc[0]) # first row of data frame (Aleshia Tomkiewicz) - Note a Series data type output.
print(data.iloc[1]) # second row of data frame (Evan Zigomalas)
print(data.iloc[-1]) # last row of data frame (Mi Richan)
# Columns:
print(data.iloc[:,0]) # first column of data frame (first_name)
print(data.iloc[:,1]) # second column of data frame (last_name)
print(data.iloc[:,-1]) # last column of data frame (id)

# Multiple row and column selections using iloc and DataFrame
print(data.iloc[0:5]) # first five rows of dataframe
print(data.iloc[:, 0:2]) # first two columns of data frame with all rows
print(data.iloc[[0,3,6,24], [0,5,6]]) # 1st, 4th, 7th, 25th row + 1st 6th 7th columns.
print(data.iloc[0:5, 5:8]) # first 5 rows and 5th, 6th, 7th columns of data frame (county -> phone1).

data.set_index("last_name", inplace=True)
print(data.head())

print(data.loc['Andrade'])
print(data.loc[['Andrade','Veness']])
print(data.loc[['Andrade','Veness'],['first_name', 'address', 'city']])

# Select rows with index values 'Andrade' and 'Veness', with all columns between 'city' and 'email'
print(data.loc[['Andrade', 'Veness'], 'city':'email'])
# Select same rows, with just 'first_name', 'address' and 'city' columns
print(data.loc['Andrade':'Veness', ['first_name', 'address', 'city']])
 
# Change the index to be based on the 'id' column
print(data.set_index('id', inplace=True))
# select the row with 'id' = 487
#data.loc[487]

print(data.loc[data['first_name'] == 'Antonio'])
print(data.loc[data['first_name'] == 'Erasmo', ['company_name', 'email', 'phone1']])

print(data.loc[data['first_name'] == 'Antonio'], 'email')
print(data.loc[data['first_name'] == 'Antonio'], ['email'])


# Select rows with first name Antonio, # and all columns between 'city' and 'email'
print(data.loc[data['first_name'] == 'Antonio', 'city':'email'])
 
# Select rows where the email column ends with 'hotmail.com', include all columns
print(data.loc[data['email'].str.endswith("hotmail.com")])  
 
# Select rows with last_name equal to some values, all columns
print(data.loc[data['first_name'].isin(['France', 'Tyisha', 'Eric'])]) 
       
# Select rows with first name Antonio AND hotmail email addresses
print(data.loc[data['email'].str.endswith("gmail.com") & (data['first_name'] == 'Antonio')])
 
# select rows with id column between 100 and 200, and just return 'postal' and 'web' columns
#print(data.loc[(data['id'] > 100) & (data['id'] <= 200), ['postal', 'web']])
 
# A lambda function that yields True/False values can also be used.
# Select rows where the company name has 4 words in it.
print(data.loc[data['company_name'].apply(lambda x: len(x.split(' ')) == 4)]) 
 
# Selections can be achieved outside of the main .loc for clarity:
# Form a separate variable with your selections:
idx = data['company_name'].apply(lambda x: len(x.split(' ')) == 4)
# Select only the True values in 'idx' and only the 3 columns specified:
print(data.loc[idx, ['email', 'first_name', 'company']])
