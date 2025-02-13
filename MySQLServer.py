import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establishing connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',      # Your MySQL host
            user='root',           # Your MySQL username
            password='password'    # Your MySQL password
        )
        
        if connection.is_connected():
            print("Successfully connected to MySQL server.")
            
            cursor = connection.cursor()
            
            # Create the database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
            
            # Close the cursor and the connection
            cursor.close()
            connection.close()

    except Error as e:
        print(f"Error: {e}")
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
