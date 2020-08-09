import sqlite3
import dbFunctions
## db config ##
conn = sqlite3.connect('db_writer/detect.db')
cursor = conn.cursor()
##########################

# cursor.execute("CREATE TABLE IF NOT EXISTS detectedPeople (date TEXT, time TEXT)")

cursor.execute("INSERT INTO detectedPeople VALUES (?, ?)", (dbFunctions.date(), dbFunctions.time()))
conn.commit()