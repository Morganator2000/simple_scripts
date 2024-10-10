'''
Use this script when you want to quickly extract only the rows from a csv that
meet a specific criteria
'''

import pandas as pd
import os

file = 'Biovigilance_Sequencing data arrangement_20240829.csv'
target_column = 'Target'
target_variable = 'fungalITS'

file_name, file_extension = os.path.splitext(file)
new_name = f"{file_name}_filtered{file_extension}"

df = pd.read_csv(file)
filtered_df = df[df[target_column] == target_variable]
filtered_df.to_csv(new_name, index=False)
