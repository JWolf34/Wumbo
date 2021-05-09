import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("google_secret.json", scope)

client = gspread.authorize(creds)

ws_multiplayer = client.open_by_key('1eBgg9IlyGam_SO7gmymqR4O_xOQ5THshz5-JyLhsMLI').worksheet('Multiplayer')

data_multiplayer = ws_multiplayer.get_all_values()

for row in data_multiplayer:
    for col in row:
        print(col)