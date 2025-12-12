import pandas as pd
import numpy as np

# create a sample dataset
data = {
    "name" : ["Asad", "Ayushi", "Taylor", np.nan, "Rehman"],
    "Age" : [20, 21, np.nan, 22, 34],
    "Score" : [np.nan, 95, np.nan, np.nan, 87]
}

df = pd.DataFrame(data)
print("Original data : \n", df)

# cleaning data

df = df.rename(columns={"name" : "first_name"})
# print(df)

# df = df.fillna(method="ffill")
# print(df)

df["Age"] = df["Age"].fillna(df["Age"].interpolate())
# print(df)

df["Score"] = df["Score"].fillna(df["Score"].mean())

print("\nCleaned data : \n", df)