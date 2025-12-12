import numpy as np
import pandas as pd

data1 = {
    "Name" : ["Asad", "Ayushi", "Rehman", "Ananya"],
    "Age" : [20, np.nan, np.nan, 30],
    "Rating" : [7, 10, 9, 10]
}

data2 = {
    "Name" : ["Asad", "Linus", "Ayushi", "Shahrukh", "Hamza"],
    "ID" : [np.random.randint(1, 100) for _ in range(5)],
    "Score" : [12, 23, 34, 21, 19]
}
df1 = pd.DataFrame(data1) 
df2 = pd.DataFrame(data2) 
print(df2)
print('\n', df1)

df = pd.merge(df1, df2, how="outer", on="Name")
print("\nMerged column : \n", df)

df["Age"] = df["Age"].fillna(df["Age"].interpolate())
df["Rating"] = df["Rating"].fillna(df["Rating"].interpolate())
df["ID"] = df["ID"].fillna(df["ID"].mean())
df["Score"] = df["Score"].fillna(df["Score"].mean())

df[["Rating", "Age", "ID", "Score"]] = df[["Rating", "Age", "ID", "Score"]].astype(int)


print("\nCleaned Data :\n", df)

"""
data 1 :
       Name  ID  Score
0      Asad  72     12
1     Linus  71     23
2    Ayushi  62     34
3  Shahrukh  91     21
4     Hamza  98     19

data 2 :
      Name   Age  Rating
0    Asad  20.0       7
1  Ayushi   NaN      10
2  Rehman   NaN       9
3  Ananya  30.0      10

Merged column :
        Name   Age  Rating    ID  Score
0    Ananya  30.0    10.0   NaN    NaN
1      Asad  20.0     7.0  72.0   12.0
2    Ayushi   NaN    10.0  62.0   34.0
3     Hamza   NaN     NaN  98.0   19.0
4     Linus   NaN     NaN  71.0   23.0
5    Rehman   NaN     9.0   NaN    NaN
6  Shahrukh   NaN     NaN  91.0   21.0

Cleaned Data :
        Name  Age  Rating  ID  Score
0    Ananya   30      10  78     21
1      Asad   20       7  72     12
2    Ayushi   20      10  62     34
3     Hamza   20       9  98     19
4     Linus   20       9  71     23
5    Rehman   20       9  78     21
6  Shahrukh   20       9  91     21
"""