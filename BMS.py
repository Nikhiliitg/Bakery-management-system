import pandas as pd
from datetime import datetime

orders = []

def add_order(date, name, order, quantity):
    orders.append({'Date': date, 'Name': name, 'Order': order, 'Quantity': quantity})
    print(f"Order added: {name} ordered {quantity} {order}(s) on {date}")
    
def view_orders():
    df = pd.DataFrame(orders)
    if df.empty:
        print("No orders yet")
    else:
        print(df)
        
def save_to_excel(filename):
    df = pd.DataFrame(orders)
    df.to_excel(filename, index=False)
    print(f"Orders saved to {filename}")
    
while True:
    print("\n____Bakery Management System____")
    print("1. Add a new Order")
    print("2. View all orders")
    print("3. Save orders to Excel")
    print("4. Exit")
    
    choice = input("Enter your choice: ").strip()
    print(f"Captured choice: {choice}")  # Debugging line
    
    if choice == "1":
        print("Option 1 selected")  # Debugging line
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        name = input("Enter your name: ")
        order = input("Enter your order: ")
        quantity = input("Enter the quantity: ")
        add_order(date, name, order, quantity)
        
    elif choice == "2":
        print("Option 2 selected")  # Debugging line
        view_orders()
        
    elif choice == "3":
        print("Option 3 selected")  # Debugging line
        filename = input("Enter the filename (with .xlsx extension): ")
        save_to_excel(filename)
        
    elif choice == "4":
        print("Exiting. Thank you! Have a good day.")
        break
        
    else:
        print("Invalid choice, please try again.")

