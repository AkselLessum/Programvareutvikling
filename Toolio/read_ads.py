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
SAMPLE_RANGE_NAME = 'Ads!A1:I17'

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
      "model": "main.ad",
      "pk": pk_counter,
      "fields": {
        "isRequest": row[values[0].index("isRequest")],
        "title": row[values[0].index("title")],
        "date": row[values[0].index("date")],
        "price": row[values[0].index("price")],
        "description": row[values[0].index("description")],
        "image": row[values[0].index("image")],
        "user": row[values[0].index("user_id")],
        "isRented": row[values[0].index("isRented")],
      }
    }
    pk_counter += 1
    data.append(value)

with open(f"ads.json", "w") as output:
    json.dump(data, output, indent=4)
    output.write("\n")