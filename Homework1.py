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

    print('Welcome to the Cougar Cafe!!!!!!\n'
              'Please select from the options below:\n'
              'Press 1 to view our full menu\n'
              'Press 2 to start an order\n'
              'Press 3 to exit\n')
    
    option = int(input("Please choose an option: "))
    
    if option == 1:
        print("Here is our full menu:\n")
        cursor.execute("SELECT item_id, item_name, item_price FROM menu")
        menu = cursor.fetchall()

        for item in menu:
            
            item_id = item['item_id']
            item_name = item['item_name']
            item_price = item['item_price']
    
            item_price = float(item_price)
            print(f"{item_id}. {item_name} - ${item_price:.2f}")

    if option == 2:
        order_items = []
        total_amount = 0.0  

    while True:
        try:
            item_input = input("\nEnter the item ID to add to your order, or type 'done' to finish: ").strip()
            if item_input.lower() == 'done':
                break
            item_id = int(item_input)

            cursor.execute("SELECT item_id, item_name, item_price FROM menu WHERE item_id = %s", (item_id,))
            item = cursor.fetchone()

            if not item:
                print("Invalid item ID. Please try again.")
                continue

            item_name = item['item_name']
            item_price = float(item['item_price'])

            order_items.append((item_name, item_price))
            total_amount += item_price
            print(f"Added '{item_name}' to your order. Current total: ${total_amount:.2f}")

        except ValueError:
            print("Invalid input. Please enter a valid item ID or 'done' to finish.")

    print("\nYour Order:")
    for idx, (name, price) in enumerate(order_items, 1):
        print(f"{idx}. {name} - ${price:.2f}")
    print(f"Total Amount: ${total_amount:.2f}")
   


if __name__ == "__main__":
    main()





