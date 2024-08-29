import pandas as pd

def check_duplicates(df):
    duplicate_rows = df[df.duplicated(keep=False)]
    if duplicate_rows.empty:
        return "No duplicate rows found"
    else:
        return duplicate_rows

input_file = 'file.csv'
data_frame = pd.read_csv(input_file)

duplicates = check_duplicates(data_frame)
print(duplicates)