import pandas as pd

def check_duplicates(df):
    duplicate_rows = df[df.duplicated(keep=False)]
    return duplicate_rows

input_file = 'Manifest_Bac16S_list.csv'
data_frame = pd.read_csv(input_file)

duplicates = check_duplicates(data_frame)
print(duplicates)