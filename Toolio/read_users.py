from googleapiclient.discovery import build
from google.oauth2 import service_account

import json


SERVICE_ACCOUNT_FILE = 'keys.json'
# If modifying these scopes, delete the file token.json.
# readonly scope, if updating the sheet is wanted then remove '.readonly'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID  of the spreadsheet
SAMPLE_SPREADSHEET_ID = '1Tas4OgAgvY6kfrJUCvT12w3tf9AedUG2d9P7_-skElE'
SAMPLE_RANGE_NAME = 'Users!A1:I12'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()

data = []
pk_counter = 90
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
values = result.get('values', [])

if not values:
  print("Empty sheet")
else:
  for row in values[1:]:
    value = {
      "model": "user.CustomUser",
      "pk": pk_counter,
      "fields": {
        "first_name": row[values[0].index("first_name")],
        "last_name": row[values[0].index("last_name")],
        "username": row[values[0].index("username")],
        "phone_number": row[values[0].index("phone_number")],
        "email": row[values[0].index("email")],
        "password": row[values[0].index("password")],
        "postal_code": row[values[0].index("postal_code")],
        "longitude": row[values[0].index("longitude")],
        "latitude": row[values[0].index("latitude")],
      }
    }
    pk_counter += 1
    data.append(value)

with open(f"users.json", "w") as output:
    json.dump(data, output, indent=4)
    output.write("\n")