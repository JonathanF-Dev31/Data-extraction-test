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

# Ruta de la carpeta con los PDFs
carpeta_pdfs = r"H:\PROYECTOS\Data extraction test\PDFs"

# Rango de coordenadas para capturar los valores deseados
x0_min, x0_max = 207, 213
x1_min, x1_max = 250, 253
top_min, top_max = 191, 193
bottom_min, bottom_max = 199, 201

def extraer_valores(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        for num_pagina, page in enumerate(pdf.pages):
            for word in page.extract_words():
                x0, x1 = word['x0'], word['x1']
                top, bottom = word['top'], word['bottom']

                # Verificar si está dentro del rango de coordenadas
                if (x0_min <= x0 <= x0_max and
                    x1_min <= x1 <= x1_max and
                    top_min <= top <= top_max and
                    bottom_min <= bottom <= bottom_max):
                    
                    print(f"✅ Encontrado en {pdf_path} - Página {num_pagina + 1}: {word['text']}")

# Analizar todos los PDFs en la carpeta
for archivo in os.listdir(carpeta_pdfs):
    if archivo.endswith(".pdf"):
        pdf_path = os.path.join(carpeta_pdfs, archivo)
        extraer_valores(pdf_path)
