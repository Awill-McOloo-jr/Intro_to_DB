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

    except mysql.connector.Error as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Ensure that the connection is closed if it was successfully created
        if connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
