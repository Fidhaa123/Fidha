import mysql.connector

def insert_data(id, name, email):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="roottoor",
        database="fidhaaa_ece"
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO people(id, name, email) VALUES (%s, %s, %s)"
    val = (id, name, email)

    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    mycursor.close()
    mydb.close()
id = input("enter the id: ")
name = input("enter the name: ")
email = input("enter the email: ")

insert_data(id, name, email)