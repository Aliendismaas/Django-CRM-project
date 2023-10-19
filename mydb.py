import mysql.connector

dataBase = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    passwd = '41810192Alien@2023-101'

)
#prepare the cusror object

cursorObject = dataBase .cursor()

#Create a Database
cursorObject.execute("CREATE DATABASE elderco")

print("all Done Successful.")