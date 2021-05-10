import pyodbc
import json
import log

with open('config.json') as config_file:
    data = json.load(config_file)

SQL_USER = data['sql'][0]['SQL_USER']
SQL_PASS = data['sql'][0]['SQL_PASS']


#TODO: Write this one
def insertUser(attributes):
    cursor = conn.cursor()
    
    
    cursor.execute(
        'INSERT INTO dbo.Users VALUES(?,?,?);',
        attributes
    )
    conn.commit()
    return 1

def insertGame(attributes):
    cursor = conn.cursor()
    
    cursor.execute(
        'INSERT INTO dbo.Games (Name, Client, WebLink, Description, Trailer, NumPlayers, BasePrice) VALUES(?,?,?,?,?,?,?);',
        attributes
    )
    conn.commit()
    return 1

def selectGameWithName(gameName):
    cursor = conn.cursor()
    gameName = '%'+ gameName + '%'
    cursor.execute(
        "SELECT TOP 5 Name FROM dbo.Games WHERE Name LIKE ?", gameName)

    games = list()
    for row in cursor.fetchall():
        games.append(row[0])

    return games

def insertSubscription(userID, gameName):
    cursor = conn.cursor()
    gameID = getGameIDfromName(gameName)

    args = [gameID, userID]
    cursor.execute(
        "INSERT INTO dbo.Subscriptions VALUES (?,?)", args
    )
    cursor.commit()

def isUserSubscribed(gameName, userID):
    cursor = conn.cursor()
    gameID = getGameIDfromName(gameName)
    args = [gameID, userID]

    cursor.execute(
        "SELECT * FROM dbo.Subscriptions WHERE GameID = ? AND UserID = ?", args
    )

    if len(cursor.fetchall()) > 0:
        return 1
    else:
        return 0


def getGameIDfromName(gameName):
    cursor = conn.cursor()
    gameName = '%'+ gameName + '%'
    cursor.execute(
        "SELECT ID FROM dbo.Games WHERE Name LIKE ?", gameName)

    gameID = cursor.fetchall()[0][0]

    return gameID







conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=168.91.234.209;"
    "Database=Wumbo;"
    "UID=" + SQL_USER + ";"
    "PWD=" + SQL_PASS + ";"
    "Trusted_Connection=no"
)

