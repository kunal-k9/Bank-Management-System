import mysql.connector as sql

mydb = sql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="bank",
)

cursor = mydb.cursor()

def createCustomerTable():
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers
               (username VARCHAR(20),
               password VARCHAR(20),
               name VARCHAR(20),
               age INTEGER,
               city VARCHAR(20),
               balance INTEGER,
               account_number INTEGER PRIMARY KEY)
    ''')

mydb.commit()

if __name__ == "__main__":
    createCustomerTable()

def db_query(query):
    cursor.execute(query)
    result = cursor.fetchall()
    return result