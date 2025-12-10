import pandas as pd

# reading files like csv, excel and more using pandas

df = pd.read_csv('Pandas/Data_set/MOCK_DATA.csv')
print(df) #to view full data

df = pd.read_csv("Pandas/Data_set/MOCK_DATA.csv")

df.to_excel('file_name') # save the data frame in the excel file like conversion

# viewing data upto 5lines from above
print(df.head())

print(df.tail(3)) # view the n numbers of data from the bottom

print(df.info()) # shows the information of the file

print(df.describe()) # shows the info of the file in a statistical way

"""
   id  first_name  ...       gender      ip_address
0   1     Diannne  ...   Polygender   136.255.70.60
1   2        Yvon  ...         Male   253.127.62.15
2   3      Emelda  ...       Female    6.233.29.125
3   4       Debby  ...       Female   186.98.84.135
4   5      Egbert  ...         Male  164.196.79.149
5   6       Myrah  ...       Female   153.61.61.152
6   7  Bartholemy  ...  Genderqueer   59.24.223.135
7   8      Oralia  ...       Female   47.155.132.12
8   9     Michale  ...         Male  156.172.59.102
9  10       Yance  ...         Male   122.236.57.63

[10 rows x 6 columns]
   id first_name  ...      gender      ip_address
0   1    Diannne  ...  Polygender   136.255.70.60
1   2       Yvon  ...        Male   253.127.62.15
2   3     Emelda  ...      Female    6.233.29.125
3   4      Debby  ...      Female   186.98.84.135
4   5     Egbert  ...        Male  164.196.79.149

[5 rows x 6 columns]
   id first_name  ...  gender      ip_address
7   8     Oralia  ...  Female   47.155.132.12
8   9    Michale  ...    Male  156.172.59.102
9  10      Yance  ...    Male   122.236.57.63

[3 rows x 6 columns]
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 6 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   id          10 non-null     int64
 1   first_name  10 non-null     object
 2   last_name   10 non-null     object
 3   email       10 non-null     object
 4   gender      10 non-null     object
 5   ip_address  10 non-null     object
dtypes: int64(1), object(5)
memory usage: 612.0+ bytes
None
             id
count  10.00000
mean    5.50000
std     3.02765
min     1.00000
25%     3.25000
50%     5.50000
75%     7.75000
max    10.00000
"""

# selecting a particular column of the file
print(df[["first_name", "last_name"]])

# filter rows of the file
print(df[df["id"] > 35])

# get first row of the file by position
print(df.iloc[0])

# get the first column of the file by position
print(df.iloc[:, 0])

# selecting by label
print(df.loc[0]) # rows
print(df.loc[:, 0]) # columns