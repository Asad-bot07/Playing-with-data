# Data aggregation and data grouping

# grouping data allows us to performs operation on the subset of data based on shared category

grouped = df.groupby('column_name') # groupby func

# iterating over the grouped data
for name, group in grouped :
    print(name)
    print(group)

# performing aggregation methods 
grouped.mean()
grouped.sum()

# Aggregation function

df.groupby('column_name')['numeric_column'].mean()

df.groupby("category_column").agg({'numeric_column' : ["max", "min", "mean"]})

pivot = df.pivot_table(values='numeric_column', index='category_column', aggfunc='mean')

# custom aggregate func

def range_func(x):
    return x.max() - x.min()

df.groupby('category_column')['numeric_column'].agg(range_func)

# calculating summary statustic for grouped data

df.groupby('categroy_column')['numeric_column'].mean()
df.groupby('categroy_column')['numeric_column'].max()
df.groupby('categroy_column')['numeric_column'].min()

# multi aggregation
df.groupby('category_column').agg({'numeric_column': [min,max, mean]})