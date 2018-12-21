import sqlite3
from sqlite3 import  Error



database = str(input("Database file name: "))
def create_conn(db_file):

    ''''Create an empty data base for Flask application '''

    try:
        Conn = sqlite3.connect(db_file)
        print("Connections found. {}".format(sqlite3.version))
    except Error as e:
        print("Error, {}".format(e))

    finally:
        Conn.close()

Connection = sqlite3.connect(database)

def Create(connection):
    c= connection.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS shop_items(name TEXT, quantitiy TEXT, price TEXT)""")
    c.execute("""CREATE TABLE IF NOT EXISTS employees(name TEXT, type TEXT, password TEXT)""")
    c.close()

def Insert(connection):
    c = connection.cursor()
    c.execute("""INSERT INTO shop_items VALUES("water", "40", "100")""")
    c.execute("""INSERT INTO shop_items VALUES("sprite&juice", "40", "110")""")
    c.execute("""INSERT INTO shop_items VALUES("candy", "100", "10")""")
    c.execute("""INSERT INTO employees VALUES("itsjasonh","2", "badone")""")
    c.execute("""INSERT INTO employees VALUES("theeguy9", "3", "f2f2")""")
    c.execute("""INSERT INTO employees VALUES("newguy29","4", "Comeon")""")
    c.execute("""INSERT INTO shop_items VALUES("Spicy_water", "40", "110")""")
    connection.commit()
    c.close()



def Use_Data(connection):
    c = connection.cursor()



    c.execute('SELECT name,password FROM employees UNION SELECT name, price FROM shop_items')

    all_rows = c.fetchall()
    print(all_rows)
    connection.commit()
    c.close()


if __name__ == "__main__":
    create_conn(database)
    Create(Connection)
    Insert(Connection)
    Use_Data(Connection)
