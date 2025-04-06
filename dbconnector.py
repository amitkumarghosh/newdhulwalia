import streamlit as st
import mysql.connector

def mydb():
    st.title("MySQL Database Connection Example")

    # Check if the secrets are set
    if "mysql" not in st.secrets:
        st.error("MySQL secrets not found. Please set them in the Streamlit secrets manager.")
        return

    # Access the secrets
    db_config = {
        'host': st.secrets["mysql"]["host"],
        'database': st.secrets["mysql"]["database"],
        'user': st.secrets["mysql"]["user"],
        'password': st.secrets["mysql"]["password"],
        'port': st.secrets["mysql"]["port"]
    }

    # Connect to the database
#     conn = mysql.connector.connect(**db_config)
#     cursor = conn.cursor()

#     # Fetch data from the database
#     cursor.execute("SELECT * FROM Attendance")
#     data = cursor.fetchall()

# # Display the data in Streamlit
# st.subheader("User Records")
# st.write(data)
# # Access the secrets
# db_config = {
# 'host': st.secrets["mysql"]["host"],
# 'database': st.secrets["mysql"]["database"],
# 'user': st.secrets["mysql"]["user"],
# 'password': st.secrets["mysql"]["password"],
# 'port': st.secrets["mysql"]["port"]
# }

# # Connect to the database
# conn = mysql.connector.connect(**db_config)
# cursor = conn.cursor()

# def fetch_data():
#     conn = mysql.connector.connect(**db_config)
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM Attendance")
#     data = cursor.fetchall()
#     conn.close()
#     return data

# st.subheader("User Records")
# data = fetch_data()
# st.write(data)