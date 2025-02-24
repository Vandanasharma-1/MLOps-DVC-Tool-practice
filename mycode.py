import pandas as pd
import os

data = {
    'Name' : ['Alice', 'Bob', 'Charlie'],
    'Age'  : [25, 30,  35],
    'city' : ['New York', 'Los Angeles', 'Chicago']
    }

df =pd.DataFrame(data)

#adding new row to df for V2
new_row_loc={'Name':'GF1', 'Age': 20, 'city':'city1'}
df.loc[len(df.index)]=new_row_loc

#adding new row again
new_row_loc2={'Name':'GF2', 'Age': 30, 'city':'city2'}
df.loc[len(df.index)]=new_row_loc2

data_dir='data'
os.makedirs(data_dir, exist_ok=True)

file_path=os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path, index=False)
print(f'File path saved to {file_path}')