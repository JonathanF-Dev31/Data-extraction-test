from google_sheet_actions import GoogleSheet
import uuid


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