import pdfplumber
import os

"""
Extracts and prints specific values from a PDF file based on coordinate ranges.
This function opens a PDF file, iterates through its pages, and extracts words.
It checks if the coordinates of each word fall within specified ranges and prints
the word if it matches the criteria.
Args:
    pdf_path (str): The file path to the PDF file to be processed.
Returns:
    None
"""

import os
import pdfplumber

# Path to the folder containing the PDFs
pdf_folder_path = r"H:\PROYECTOS\Data extraction test\PDFs"

# Coordinate range to capture the desired values
x0_min, x0_max = 207, 213
x1_min, x1_max = 250, 253
top_min, top_max = 191, 193
bottom_min, bottom_max = 199, 201

def extract_values(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            for word in page.extract_words():
                x0, x1 = word['x0'], word['x1']
                top, bottom = word['top'], word['bottom']

                # Check if it's within the coordinate range
                if (x0_min <= x0 <= x0_max and
                    x1_min <= x1 <= x1_max and
                    top_min <= top <= top_max and
                    bottom_min <= bottom <= bottom_max):

                    print(f"✅ Found in {pdf_path} - Page {page_num + 1}: {word['text']}")

# Analyze all PDFs in the folder
for file_name in os.listdir(pdf_folder_path):
    if file_name.endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder_path, file_name)
        extract_values(pdf_path)