import streamlit as st
import pandas as pd
from datetime import datetime

# Initialize the orders list in session_state if it doesn't exist
if 'orders' not in st.session_state:
    st.session_state['orders'] = []

# Function to add an order
def add_order(date, name, order, quantity):
    st.session_state['orders'].append({'Date': date, 'Name': name, 'Order': order, 'Quantity': quantity})
    st.success(f"Order added: {name} ordered {quantity} {order}(s) on {date}")

# Function to view all orders
def view_orders():
    if st.session_state['orders']:
        df = pd.DataFrame(st.session_state['orders'])
        st.write(df)
    else:
        st.warning("No orders yet")

# Function to save orders to an Excel file
def save_to_excel(filename):
    df = pd.DataFrame(st.session_state['orders'])
    df.to_excel(filename, index=False)
    st.success(f"Orders saved to {filename}")

# Streamlit layout and app logic
st.title("Bakery Management System")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = ["Add Order", "View Orders", "Save Orders to Excel", "Exit"]
choice = st.sidebar.selectbox("Choose an action", options)

# Add order section
if choice == "Add Order":
    st.header("Add a New Order")
    name = st.text_input("Enter your name:")
    order = st.text_input("Enter your order:")
    quantity = st.number_input("Enter quantity:", min_value=1, step=1)
    if st.button("Add Order"):
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        add_order(date, name, order, quantity)

# View orders section
elif choice == "View Orders":
    st.header("All Orders")
    view_orders()

# Save orders to Excel section
elif choice == "Save Orders to Excel":
    st.header("Save Orders to Excel")
    filename = st.text_input("Enter filename (with .xlsx extension):")
    if st.button("Save Orders"):
        if filename:
            save_to_excel(filename)
        else:
            st.error("Please provide a valid filename.")

# Exit section
elif choice == "Exit":
    st.write("Thank you for using the Bakery Management System!")
    st.stop()  # Stops the Streamlit app
