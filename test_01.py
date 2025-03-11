import PyPDF2
import os
import re
from test_02 import insert_data

"""
Extracts income information from PDF files and uploads the extracted data to Google Sheets.

This script scans a specified folder for PDF files, extracts text from each document, and applies
regular expressions to retrieve the owner's name and total gross equity. The extracted information
is then stored in a Google Sheet for further analysis.

Dependencies:
- PyPDF2: For reading PDF content
- re: For applying regular expressions

Args:
    pdf_path (str): The file path to the PDF file.

Returns:
    None: The extracted information is uploaded to Google Sheets.
"""

def exract_income_info(pdf_path):
    #open the pdf file
    with open(pdf_path, "rb") as file:
        #Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        # Extract text from each page on the PDF file
        text = ''

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

              
        # Regular expression to find the income
        name_owner_pattern = r"\d{10,}\s*\d*([A-ZÁÉÍÓÚÑ ]{5,})"
        total_gross_equity_pattern = r"(\d{1,3}(?:,\d{3}){1,3})"

        # Extract information using regular expressions
        name_owner_match = re.search(name_owner_pattern, text)
        total_gross_equity_matches = re.findall(total_gross_equity_pattern, text)

        # Convert the gross income to a number
        total_gross_equity_matches = [int(item.replace(',','')) for item in total_gross_equity_matches]
        
        # Extracted information
        name_owner = name_owner_match.group(1) if name_owner_match else None

        total_gross_equity = max(total_gross_equity_matches) if len(total_gross_equity_matches) > 0 else "No encontrado"
        
        print(f"File: {pdf_path}")
        print(f"Name owner: {name_owner}")
        print(f"Total gross equity: {total_gross_equity}")

        return name_owner, total_gross_equity

pdf_path_folder = "H:\\PROYECTOS\\Data extraction test\\PDFs"


name_owner, total_gross_equity = '', ''
for file_name in os.listdir(pdf_path_folder):
    if file_name.endswith(".pdf"):
        file_path = os.path.join(pdf_path_folder, file_name)
        name_owner, total_gross_equity = exract_income_info(file_path)
        insert_data(name_owner, total_gross_equity)
