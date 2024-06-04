__authors__ = "Morgan Bakelmun"
__maintainer__ = "Morgan Bakelmun"
__email__ = "morganbakelmun@hotmail.com"

import pandas as pd

# This script will go through each sample column and determine which taxa and 
# ASV are the most abundant in a sample.

CODE_TYPE = 'latin1' # https://docs.python.org/3/library/codecs.html#standard-encodings
input_file = 'feature-table.csv' #Location of the input data. Use a relative path.
asv_column = '#OTU ID'#Change this if your ASV column is called something else.
taxa_column = 'Taxon' #Change this if your OTU column is called something else.
non_samples = [asv_column,taxa_column]

df = pd.read_csv(input_file)
sample_columns = [col for col in df.columns if col not in non_samples]
results = []

# Process each sample column
for column in sample_columns:
    # Find the row with the maximum count for the current sample column
    max_idx = df[column].idxmax()
    max_row = df.loc[max_idx]
    
    # Append the sample name, ID, and Animal to the results list
    results.append({
        'Sample': column,
        taxa_column: max_row[taxa_column],
        asv_column: max_row[asv_column]
    })

# Create a new DataFrame from the results list
results_df = pd.DataFrame(results)

# Write the results DataFrame to a new CSV file
results_df.to_csv('results.csv', index=False)
