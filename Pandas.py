
# Import Pandas and open CSV file. // EXcel file is opened the same way

my_dict = { 'Name':['Hassan', 'Arslan', 'Noman', 'Ahmed', 'Bilal', 'David', 'Joshua', 'Kent', 'Dwayne'],
            'Location':['Islamabad', 'Lahore', 'Lahore', 'Sargodha', 'Peshawar', 'London','Stuttgurt','Sydney','Tokyo'],
            'Phone': ['051','042','042','063','056','902','611','432','989']} # Create a dictionary

import pandas as pd;
file_path = "D:\\Data Science\\Data Sets\\annual-balance-sheets-and-accumulation-accounts-200817-provisional-csv.csv"
data_set = pd.read_csv(file_path);

print(data_set.head()) # Print first 5 rows of the data set
print(data_set) # Print complete data set

dict_ds = pd.DataFrame(my_dict); # Converting the Dictionary into a Panda Data Set
print(dict_ds) # Print the Data Set

# you can create multiple data sets from one data set by selecting the columns
name_phone_ds = dict_ds[['Name','Phone']]; # Create a new Data set of Column Name & Phone
print(name_phone_ds)

# Using LOC -------- ILOC ----------- IX to Access the data set

# LOC takes 1 integer and Column/Row name as a parameter
print(dict_ds.loc[4,'Phone']) # 4th Row and Column "Phone"

# ILOC takes both numbers as parameters
print(dict_ds.iloc[4,2]) # 4th Row and Column 2nd Column, Will give the same result as above LOC command

# ------- CREATE NEW DATA SET WITH LOC SLICING
sliced_ds = dict_ds.loc[0:3,'Name':'Phone'] # slice the data set from 0-3 rows and between "Name" & "Phone" column
print(sliced_ds)

# ------- CREATE NEW DATA SET WITH iLOC SLICING
sliced_ds2 = dict_ds.iloc[0:3,0:2] # slice the data set from 0-3 rows and between 0-2(Minus 1) columns
print(sliced_ds2)

# Using Unique Function to Determine the Unique Elements in a Data Frame

unique_ds = data_set['Institutional_sector_code'].unique(); # Will Give Unique Value in this column
print(unique_ds)

# Creating a New Data Set and Saving in CSV File
sub_data_set = data_set[data_set['Year'] >= 2009] # Will create a new Data set for Year after 2009
print(sub_data_set)
print(sub_data_set.head())
sub_data_set.to_csv('Sub_Data_set.csv') # Create a new CSV file and save, There are a lot of formats which we can save the data set into

