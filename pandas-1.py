import pandas as pd 

order = pd.read_table('https://github.com/AshishGavit/data-source/blob/main/chiporders.tsv?raw=True')

print(order.head())

user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
user_detail = pd.read_table('https://github.com/AshishGavit/data-source/blob/main/movieusers.tsv?raw=True', sep='|', header=None, names=user_cols)

print(user_detail.head())