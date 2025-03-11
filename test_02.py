from google_sheet_actions import GoogleSheet
import uuid

"""
Module for inserting extracted income data into Google Sheets.

This script provides functionality to generate a unique identifier (UUID) and insert extracted income data 
(owner's name and total gross equity) into a specified Google Sheet.

Dependencies:
- google_sheet_actions.GoogleSheet: Handles interactions with Google Sheets.
- uuid: Generates unique identifiers.

Functions:
- generate_uid(): Generates a unique identifier as a string.
- insert_data(name_owner, total_gross_equity): Inserts the extracted income data into the Google Sheet.

Google Sheets Configuration:
- file_name_gs: JSON credentials file for Google Sheets API.
- google_sheet: The name of the Google Sheet.
- sheet_name: The specific sheet within the Google Sheet where data will be written.

Args for insert_data():
- name_owner (str): The name of the income owner extracted from a document.
- total_gross_equity (int/str): The extracted total gross equity.

Usage:
Call `insert_data(name_owner, total_gross_equity)` to store extracted information in Google Sheets.
"""


file_name_gs = "data-extraction-tests-495076c0f01a.json"
google_sheet = "test"
sheet_name = "sheet test"

def generate_uid():
    """
    Generate a unique identifier  
    returns:
        str: id
    """
    unique_id = uuid.uuid4()
    # Convert the UUID to a string
    return str(unique_id)

def insert_data(name_owner, total_gross_equity):
    uid = generate_uid()
    google = GoogleSheet(file_name_gs, google_sheet, sheet_name)
    value = [[uid, name_owner, total_gross_equity]]
    range = google.get_last_row_range()
    google.write_data(range, value)