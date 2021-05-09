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




conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=168.91.234.209;"
    "Database=Wumbo;"
    "UID=" + SQL_USER + ";"
    "PWD=" + SQL_PASS + ";"
    "Trusted_Connection=no"
)

