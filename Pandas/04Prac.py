# handling missing values

import pandas as pd

df = pd.read_csv('Pandas/Data_set/MOCK_DATA.csv')

df = df.dropna() #it will drop rows with missing values

df = df.dropna(axis=1) # it will drop column with missign values

df["column_name"] = df["column_name"].fillna(0) # this will fill the columns which have missing values with 0 or any numbers as we need the column and cannot just drop it

# forward fill
df = df.fillna(method="ffill")

# backward fill
df = df.fillna(method="bfill")

# interpolation way
df["column_name"] = df["column_name"].interpolate()