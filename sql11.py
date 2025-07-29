import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="roottoor",
    database="fidhaaa_ece"
)
mycursor = mydb.cursor()
mycursor.execute("select * from people")
result = mycursor.fetchall()
for row in result:
    print(row)



mydb.commit()
print(mycursor.rowcount, "record inserted.")
mycursor.close()
mydb.close()


