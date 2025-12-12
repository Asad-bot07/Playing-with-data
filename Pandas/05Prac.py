# data transformation

import pandas as pd 

df = pd.read_csv('Pandas/Data_set/MOCK_DATA.csv')

# to rename a particular column
df = df.rename(columns={"id" : "number"})

# to convert the data type of the data in any column
df["column_name"] = df["column_name"].astype("float") # you can convert it into any data type

# this converts a the data of a certain column into date and time format
df["number"] = pd.to_datetime(df["number"])
# print(df.head())

# this allows u to create a new column with data manipulated ny your wish like mul, add, or any operation to a existing column
df["new_column"] = df["existing_column"] * 2

# combining and merging dataframes

# concatenation
combined_rows = pd.concat([df1, df2], axis=0) # this concat the dataframes along rows

combined_column = pd.concat([df1, df2], axis=1) # this concat the dataframes along columns

# to merge two data set
merge_set = pd.merge(df1, df2, on="common_column" ) # with this method we can merge two data set with respect to a common column in both the data set

merged = pd.merge(df1, df2, how="left", on="common_column")
merged = pd.merge(df1, df2, how="inner", on="common_column")

# joining data frames

join = df1.join(df2, how="inner")