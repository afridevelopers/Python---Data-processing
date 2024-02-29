############################################## CHECKING INVENTORY ###################################################
import os
from datetime import datetime
import sys  

print('Checking Inventory')
# Getting the current date
current_date = datetime.now()
# Formatting the date as a string in the desired format (day.month)
formatted_date = current_date.strftime('%d.%m')

# Function to check if the path contains a valid file
def validate_path(path):
    return os.path.isfile(path)

# Example usage with multiple paths
complete_paths = [
    f'C:\\Users\\NAME\\Documents\\2024\\base1\\INVENTORY_BLUE_493_{formatted_date}.csv',
    f'C:\\Users\\NAME\\Documents\\2024\\base2\\INV{formatted_date}.csv',
    f'C:\\Users\\NAME\\Documents\\2024\\base1\\INVENTORY_BLUE_493{formatted_date}.csv',
    f'C:\\Users\\NAME\\Documents\\2024\\base2\\INVENTORY_YELLOW_086_{formatted_date}.csv',
    # Add more paths as needed
]

# List to store missing paths
missing_paths = []

# Loop to check each path
for complete_path in complete_paths:
    if validate_path(complete_path):
        print(f'\n{complete_path} OK\n---------------------------------------------------------------------')
    else:
        print(f'\nThe path {complete_path} does not contain a valid file or the file does not exist. Check the folder and filename\n')
        missing_paths.append(complete_path)

# Check for missing paths and inform
if missing_paths:
    print("\nMissing inventories:")
    for missing_path in missing_paths:
        print(missing_path)
    sys.exit("The program has been forced to stop due to missing files.")
else:
    # If all paths were successfully checked
    print("Check completed. All files are present.")

############################################## BASE PROCESSING ###################################################
print('Processing Bases')
# Importing necessary libraries
import pandas as pd  # For tabular data manipulation
from unidecode import unidecode  # Importing the unidecode function

# Complete path of the inventory
file_path = f'C://Users//gle//Documents//INVENTORY_{formatted_date}.csv'#REMEMBER TO CHANGE THE NAME IN THE COMPANY>>>>><<<<<<<<<<<

# Reading the CSV file
inventory = pd.read_csv(file_path, sep=';')

# Function to add leading zeros to CPFs with less than 11 digits
def format_cpf(cpf):
    cpf_str = str(cpf)
    zeros_to_add = 11 - len(cpf_str)
    formatted_cpf = '0' * zeros_to_add + cpf_str
    return formatted_cpf

# Applying the function to the CPF column
inventory['CPF'] = inventory['CPF'].apply(format_cpf)

# Removing duplicate CPFs
processed_inventory = inventory.drop_duplicates(subset='CPF', keep='first')
print('Finishing Base Processing')

######################################## FINISHES BASE PROCESSING ##############################################


############################################## LAYOUT PROCESSING #######################################################
print('Processing Layout1')

# Path for the CSV LAYOUT
new_file_path1 = f'C://Office//BASE II//PROCESSED_BASE_ACCOUNT{formatted_date}.csv'

# Creating a new DataFrame with only the desired columns
layout1 = pd.DataFrame(columns=['NAME', 'CPF/CNPJ', '', '', 'DAYS_DELAY', '', '', 'CONTRACT', '', 'STATE', 'STATE', 'STATE', 'STATE', '', 'WILDCARD_17'])

# Filling in the information from the new DataFrame into the corresponding columns
layout1['NAME'] = processed_inventory['NAME'].apply(lambda x: unidecode(str(x))) 
layout1['CPF/CNPJ'] = processed_inventory['CPF']
layout1['DAYS_DELAY'] = processed_inventory['DD']
layout1['CONTRACT'] = processed_inventory['CONTRACT']
layout1['STATE'] = processed_inventory['WILDCARD1']
layout1['WILDCARD_17'] = processed_inventory['PHONE']

# Adding new columns and filling them with desired values
layout1['PORTFOLIO'] = '496'
layout1['CONTACT_0800'] = '08005650404'

# Removing rows with duplicate CPFs
layout1 = layout1.drop_duplicates(subset='CPF/CNPJ', keep='first')

# Converting the CPF, CONTACT0800, and CONTRACT columns to text
layout1['CPF/CNPJ'] = layout1['CPF/CNPJ'].astype(str)
layout1['CONTRACT'] = layout1['CONTRACT'].astype(str)
layout1['CONTACT_0800'] = layout1['CONTACT_0800'].astype(str)

# Ensuring that WILDCARD_17 is filtered with values only of 11 digits
layout1 = layout1[layout1['WILDCARD_17'].str.len() == 11]

# Dropping null values
layout1.dropna()

# Saving the new DataFrame to the CSV file with UTF-8 encoding with BOM ('utf-8-sig')
layout1.to_csv(new_file_path1, index=False, encoding='utf-8-sig', sep=';')

print('Layout1 completed')

############################################# FINISHES LAYOUT PROCESSING ###################################################


############################################### SENDING EMAIL ####################################################
print('Checking if the file is empty')
import win32com.client as win32

def check_csv_file(file_path):
    # Load the CSV file using pandas
    try:
        df = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        return False  # Empty file (only header)
    
    # Check if there are data beyond the header
    return len(df) > 0

print('File checked')

def send_email(recipients, subject,  attachment_path, image_path):
    # Check if the CSV file contains data
    if check_csv_file(attachment_path):
        outlook = win32.Dispatch('Outlook.Application')
        email = outlook.CreateItem(0)
        email.To = ';'.join(recipients)
        email.Subject = subject

        # Configuring the email body
        email_body = f'''
            <html>
                <body>
                    Good morning!<br><br>
                    Dear,<br>
                    Here is the Digital Base for activation<br><br>
                    Best regards.<br><br>
                    <img src="data:image/png;base64,{get_base64_image(image_path)}">
                </body>
            </html>
        '''

        # Add the attachment
        attachment = email.Attachments.Add(attachment_path)

        # Update the email body
        email.HTMLBody = email_body

        # Send the email
        email.Send()
        print("Email sent successfully!")
    else:
        print("The CSV file is empty. The email will not be sent.")

def get_base64_image(image_path):
    import base64

    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode("utf-8")
    
    return base64_image

# Example usage with attachment
recipients = ['email1@gmail.com', 'email2@gmail.com']
subject = 'DIGITAL BASES'

attachment_path = f'C://Office//BASE II//PROCESSED_BASE_ACCOUNT{formatted_date}.csv'

# Replace the image path with the correct path for your image
image_path = 'C:/Users/gle/Downloads/signature.png'

send_email(recipients, subject, attachment_path, image_path)
