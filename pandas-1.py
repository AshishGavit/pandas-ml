import pandas as pd 

order = pd.read_table('http://bit.ly/chiporders')

print(order.head())

user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
user_detail = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_cols)

print(movies.head())