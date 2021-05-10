import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sql

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("google_secret.json", scope)
client = gspread.authorize(creds)


"""
    Initial crawl for google sheets game data. Reserved for later use, but not necessary to use while the bot is running.
"""
def getMultiplayerGameDataInit():
    ws_multiplayer = client.open_by_key('1eBgg9IlyGam_SO7gmymqR4O_xOQ5THshz5-JyLhsMLI').worksheet('Multiplayer')

    gameCols ={
        "NAME":1,
        "CLIENT":2,
        "WEBLINK":3,
        "DESCRIPTION":4,
        "TRAILER":5,
        "NUMPLAYERS":6,
        "BASEPRICE":7
    }

    gameData = list()

    for key in gameCols.keys():
        gameData.append(ws_multiplayer.col_values(gameCols.get(key)))

    for i in range(1, len(gameData[0])):
        game_attrs = list()
        for key in gameCols.keys():
            data = gameData[gameCols.get(key)-1][i]

            if data == "N/A":
                game_attrs.append(0)
            elif data == "FREE":
                game_attrs.append(0.00)
            elif "$" in data:
                game_attrs.append(float(data[1:]))
            else:
                game_attrs.append(data)    
        insertGameData(game_attrs)

def insertGameData(attributes):
    sql.insertGame(attributes)

if __name__ == "__main__":
   # getMultiplayerGameDataInit()