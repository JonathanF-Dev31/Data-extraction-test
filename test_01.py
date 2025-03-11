import PyPDF2
import os
import re
from test_02 import insert_data

"""
Extracts income information from a PDF file.
This function opens a PDF file, extracts text from each page, and uses regular expressions to find and extract the name of the owner and the total gross equity.
Args:
    pdf_path (str): The file path to the PDF file.
Returns:
    None: This function prints the extracted information (name owner and total gross equity) to the console.
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
