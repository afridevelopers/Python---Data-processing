import pandas as pd
import os

# Loading data from the stock file
stock_path = 'C:\\Users\\name\\Documents\\1\\estoque\\esto2.csv'
stock = pd.read_csv(stock_path, delimiter=';', converters={'CONTRATO': str, 'CPF': str})

# Loading data from the inconsistencies file
inconsistencies_path = 'C:\\Users\\name\\Documents\\1\\inco\\INCO2.csv'
inconsistencies = pd.read_csv(inconsistencies_path, converters={'CONTRATO': str})

# Converting all CONTRACTs to uppercase
stock['CONTRATO'] = stock['CONTRATO'].str.upper()
inconsistencies['CONTRATO'] = inconsistencies['CONTRATO'].str.upper()

# Searching for CPFs corresponding to CONTRACTs in 'inconsistencies'
results = pd.merge(inconsistencies, stock, on='CONTRATO', how='left')

# Extracting information from the 'CPF' column, adjusting if the column name varies
CPF_column = results['unnamed: 1'] if 'unnamed: 1' in results.columns else results['CPF']

# Removing duplicates and adjusting the CPF format
CPF_column = CPF_column.drop_duplicates().apply(lambda x: str(x).zfill(11))

# Asking the user for the file name
file_name = 'doc'

# Building the full path of the TXT file
file_path = f'C:\\Users\\name\\Downloads\\{file_name}.txt'

# Saving CPFs to the TXT file without the last line break after the last CPF
with open(file_path, 'w') as f:
    f.write(CPF_column.str.cat(sep=os.linesep))

print(f"CPFs have been saved in the file: {file_path}")
