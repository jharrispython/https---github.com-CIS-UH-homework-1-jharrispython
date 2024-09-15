import mysql.connector
from mysql.connector import Error

def create_con(hostname, username, userpw, dbname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = hostname,
            user = username,
            password = 'UHcougars28',
            database = dbname
        )
        print("connection successfull")

    except Error as e:
        print(f'the error {e} occured')
    return connection

conn = create_con('cis2368fall.cfe4cqq8sj4h.us-east-1.rds.amazonaws.com', 'admin', 'cis2368fall', 
                   'cis2368falldb')

cursor = conn.cursor(dictionary = True)

sql = "SELECT * FROM menu"


def main():

    option = int(input('Welcome to the Cougar Cafe!!!!!!\n'
              'Please select from the options below:\n'
              'Press 1 to view our full menu\n'
              'Press 2 to start an order\n'
              'Press 3 to exit\n'))
    
    if option == 1:
        cursor.execute(sql)
        rows = cursor.fetchall()

        for x in rows:
            
            print(x)

if __name__ == "__main__":
    main()