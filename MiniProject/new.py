import pandas as pd
import qrcode
from tkinter import Tk, filedialog, Label, Button, Entry, messagebox
import sqlite3
import os
from fpdf import FPDF
from PIL import Image
from pyzbar.pyzbar import decode


def init_db():
    conn = sqlite3.connect("qr_data.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS qr_codes (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        registration TEXT,
                        qr_path TEXT
                    )''')
    conn.commit()
    conn.close()


def save_to_db(name, registration, qr_path):
    conn = sqlite3.connect("qr_data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO qr_codes (name, registration, qr_path) VALUES (?, ?, ?)", 
                   (name, registration, qr_path))
    conn.commit()
    conn.close()

def generate_qr_codes(excel_file, data_column, name_column):
    df = pd.read_excel(excel_file)
    qr_dir = "QR_Codes"
    os.makedirs(qr_dir, exist_ok=True)
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Generated QR Codes", ln=True, align="C")

    for index, row in df.iterrows():
        qr_data = f"Name: {row[name_column]}, Registration: {row[data_column]}"
        qr_name = str(row[name_column])
        qr_path = os.path.join(qr_dir, f"{qr_name}.png")

        qr = qrcode.make(qr_data)
        qr.save(qr_path)
        
        
        decoded_data = decode(Image.open(qr_path))
        if decoded_data and decoded_data[0].data.decode("utf-8") == qr_data:
            save_to_db(qr_name, row[data_column], qr_path)
            
           
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, f"Name: {qr_name}, Registration: {row[data_column]}", ln=True)
            pdf.image(qr_path, w=30, h=30)
            pdf.ln(10)
        else:
            print(f"Error in QR validation for {qr_name}. Skipping.")

    pdf_output = "Generated_QR_Codes.pdf"
    pdf.output(pdf_output)
    messagebox.showinfo("Success", f"QR codes generated and saved to {pdf_output}")


def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    excel_entry.delete(0, 'end')
    excel_entry.insert(0, file_path)

def start_process():
    excel_file = excel_entry.get()
    data_column = data_column_entry.get()
    name_column = name_column_entry.get()

    if not excel_file or not data_column or not name_column:
        messagebox.showerror("Error", "Please fill out all fields")
        return

    generate_qr_codes(excel_file, data_column, name_column)


app = Tk()
app.title("QR Code Generator")
app.geometry("400x250")

Label(app, text="Select Excel File:").grid(row=0, column=0, padx=10, pady=10)
excel_entry = Entry(app, width=40)
excel_entry.grid(row=0, column=1)
Button(app, text="Browse", command=open_file_dialog).grid(row=0, column=2)

Label(app, text="Data Column (e.g., Registration):").grid(row=1, column=0, padx=10, pady=10)
data_column_entry = Entry(app, width=40)
data_column_entry.grid(row=1, column=1)

Label(app, text="Name Column (e.g., Name):").grid(row=2, column=0, padx=10, pady=10)
name_column_entry = Entry(app, width=40)
name_column_entry.grid(row=2, column=1)

Button(app, text="Generate QR Codes", command=start_process).grid(row=3, column=1, pady=20)


init_db()
app.mainloop()
