QR Code Automation System

Introduction
The QR Code Automation System is a Python-based desktop application that automates the generation of QR codes from data stored in an Excel file. The application allows users to select columns for names and details, validates the generated QR codes, saves their details in an SQLite database, and creates a PDF report containing all the QR codes with associated information. This project is ideal for use cases such as event management, attendance tracking, and inventory systems.


Prerequisites
Software Requirements-
- Python 3.7+: Ensure Python is installed on your system.
- Excel File: An Excel file containing the data to be converted into QR codes.

Required Python Libraries-
Install the following libraries before running the project:
pip install pandas qrcode tkinter fpdf pillow pyzbar

Other Tools-
- Any standard text editor or IDE for Python development.


How It Works-
1. Input File: The user selects an Excel file containing the data through the GUI.
2. Column Selection: The user specifies the columns for "Name" and "Registration Details" (or similar data).
3. QR Code Generation: The application generates QR codes for each entry, validates them, and saves them as PNG files.
4. Database Storage: Each QR code's data is stored in an SQLite database for future reference.
5. PDF Report: A PDF file is created containing the generated QR codes along with their details.
6. Output: The QR codes, PDF report, and database are saved in the project directory.


Features
- User-Friendly GUI: Select files and input columns easily.
- Bulk QR Code Generation: Automates the process for multiple entries.
- Validation: Ensures each QR code is generated correctly.
- Database Integration: Saves QR details in an SQLite database for persistence.
- PDF Report: Compiles QR codes into a shareable PDF document.


Usage
1. Clone this repository.
2. Install the required libraries.
3. Run the `main.py` file to launch the application.
4. Follow the on-screen instructions to upload an Excel file and generate QR codes.


Additional Notes
- Ensure that the Excel file columns match the ones specified in the GUI (e.g., "Name" and "Registration").
- All generated files (QR codes, PDF, and database) are saved in the project directory.
- This project can be extended to include features like custom QR design, email integration, or cloud storage.



Future Improvements
- Add dropdowns for column selection based on Excel file headers.
- Implement error correction levels in QR codes for enhanced reliability.
- Provide an option to clean up temporary files after generating the PDF report.
- Extend the functionality for batch processing of multiple Excel files.

