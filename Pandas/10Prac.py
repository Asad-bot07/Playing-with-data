import pandas as pd
import numpy as np

data = {
    "Class" : ["A", "B", "C", "A", "C"],
    "Score" : [85, 98, 88, 72, 99],
    "Age" : [18, 20, 19, 14, 17]
}

df = pd.DataFrame(data)
# print(df)

grouped = df.groupby("Class").sum()
print("Sum as per the class : \n", grouped)

grouped = df.groupby("Class").mean()
print("Mean as per the class :\n", grouped)

stats = df.groupby("Class").agg({"Score" : ["mean", "max", "min"], "Age" : ["mean", "max", "min"]})
print("Stats of the each column :\n", stats)
"""
       Score           Age
       mean max min  mean max min
Class
A      78.5  85  72  16.0  18  14
B      98.0  98  98  20.0  20  20
C      93.5  99  88  18.0  19  17
"""

eg = df.groupby("Class")["Score"].mean()
print(eg)

pivot = df.pivot_table(
    values="Score",
    index="Class",
    aggfunc="mean"
)
print(pivot)