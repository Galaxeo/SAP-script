import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Open spreadsheet by using the key in the URL
sheet = client.open_by_key("1fy6qiIv6CoGAG4C7EOaUrRgKjJBttqCsQoQhwZzgXU8").sheet1
# Extract values into a dictionary
list_of_hashes = sheet.get_all_records()
for item in list_of_hashes:
    print(item["Phone IP"], "Section", item["Section"], "Row", item["Row"])
