# Automation of Processes with Python 🐍

🚀 Automating tasks for inventory checking, data processing, and email sending in Python.

## Checking Inventory 📦

- The script verifies if the paths lead to valid files.
- It iterates over the list of complete paths.
- Uses the `validate_path` function to check validity.

## Base Processing 🛠️

- Utilizes the `pandas` library for tabular data manipulation.
- Formats CPFs, removes duplicates, and creates the `processed_inventory` DataFrame.
- Saves the final result to a CSV file.

## Layout Processing 📑

- Performs layout processing of the data.
- Creates the `layout1` DataFrame with specific columns and new additions.
- The final result is saved in a new CSV file.

## Sending Email 📧

- Checks if the generated CSV file is not empty.
- Uses `win32com.client` to send emails with attachments.
- Formats the email body in HTML and includes an image.

### Additional Features:

- Functions to check if the CSV file is empty and to obtain base64 encoding of an image.

### Next Step:

# Example usage with an attachment
recipients = ['user@example.com', 'anotheruser@example.com']
subject = 'DIGITAL BASES'

attachment_path = 'C://Office//BASE II//PROCESSED_BASE_ACCOUNT{formatted_date}.csv'

# Replace the image path with the correct path for your image
image_path = 'C:/Users/username/Downloads/signature.png'

send_email(recipients, subject, attachment_path, image_path)


Adjust the paths and parameters as necessary for your environment.