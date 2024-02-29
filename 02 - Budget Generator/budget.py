from tkinter import *
from fpdf import FPDF
import webbrowser

def generate_quote():
    description = entry_description.get()
    estimated_hours = entry_hours.get()
    hourly_rate = entry_hourly_rate.get().replace(",", ".")  # Replace commas with dots
    deadline = entry_deadline.get()

    total_amount = float(estimated_hours) * float(hourly_rate)

    # Generating PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial")

    # PDF coordinates/path
    pdf.image("template.png", x=0, y=0)
    pdf.text(115, 145, description)
    pdf.text(115, 160, estimated_hours)
    pdf.text(115, 175, hourly_rate)
    pdf.text(115, 190, deadline)
    pdf.text(115, 205, str(total_amount))

    pdf_file_path = "Quote.pdf"
    pdf.output(pdf_file_path)
    print("Quote generated successfully")

    # Open the file in the web browser
    webbrowser.open(pdf_file_path)

# Configuring the graphical interface
root = Tk()
root.title("Quote Generator")

# Increasing the window size
root.geometry("600x400")

label_description = Label(root, text="Project description:", font=("Arial", 12))
label_description.grid(row=0, column=0, pady=10, padx=10)
entry_description = Entry(root, font=("Arial", 12))
entry_description.grid(row=0, column=1, pady=10, padx=10)

label_hours = Label(root, text="Estimated hours:", font=("Arial", 12))
label_hours.grid(row=1, column=0, pady=10, padx=10)
entry_hours = Entry(root, font=("Arial", 12))
entry_hours.grid(row=1, column=1, pady=10, padx=10)

label_hourly_rate = Label(root, text="Hourly rate:", font=("Arial", 12))
label_hourly_rate.grid(row=2, column=0, pady=10, padx=10)
entry_hourly_rate = Entry(root, font=("Arial", 12))
entry_hourly_rate.grid(row=2, column=1, pady=10, padx=10)

label_deadline = Label(root, text="Estimated deadline in days:", font=("Arial", 12))
label_deadline.grid(row=3, column=0, pady=10, padx=10)
entry_deadline = Entry(root, font=("Arial", 12))
entry_deadline.grid(row=3, column=1, pady=10, padx=10)

button_generate = Button(root, text="Generate Quote", command=generate_quote, font=("Arial", 12))
button_generate.grid(row=4, columnspan=2, pady=20)

root.mainloop()
