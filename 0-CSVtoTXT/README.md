# CSVtoTXT

# Data Manipulation Python Script

This Python script was developed to perform manipulations on data from CSV files, adjusting formats, and generating a TXT file containing specific information.

## Objective
The main objective of the script is to provide an automated solution for processing stock and inconsistency data, searching for corresponding CPFs (Brazilian identification numbers) and saving them in a TXT file.

## Features
- **Data Reading:** The script reads data from two CSV files representing stock and inconsistency information.
- **Data Adjustments:** It performs adjustments on the data, such as formatting the 'contract' column as a string and removing symbols from CPFs.
- **Data Merging:** It merges stock and inconsistency data based on the 'contract' column.
- **Information Extraction:** It extracts and adjusts information from the 'cpf' column, removing duplicates if necessary.
- **TXT File Generation:** It prompts the user for the desired TXT file name and saves the adjusted CPFs in the file.

## How to Execute
Make sure to have Python installed, along with the pandas module. Also, adjust the paths of the CSV files as needed. During execution, follow the instructions to provide the desired TXT file name.

**Note:** If errors related to escape characters occur, use the r prefix before paths, indicating that they are "raw strings." For example:
```python
path = r'C:\path\to\your\file.csv'
