import pandas as pd

# Pandas is a powerful python libraries for data manipulation and analysis which provides data structure as Series and Data frames

# Series is an one dimensional data structure with labels which can store any data set

# data frames is a 2 dimensional labeled data structrue

# series
series = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(series)

# dataframe
data = {"name" : ["Asad", "Ayushi"], "Age": [20, 21]}
# print(data)
df = pd.DataFrame(data)
print(df)