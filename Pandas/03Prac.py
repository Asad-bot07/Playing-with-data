import pandas as pd

# loading dataset
df = pd.read_csv('Pandas/Data_set/Iris.csv')

# read first 5 rows
print("First 5 data from the file : \n", df.head())

# read last n rows
print("Last n/5 rows of data from the file :\n", df.tail(5))

# inforation about the data
print("\n")
print(df.info())

# information in stats way
print('\n')
print(df.describe())

# Select specific column and filter rows
print("Selected column :\n ",df["Species"])

print(df[df["Id"] > 145])