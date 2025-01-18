# ------------------------------------------------------
# File: test_db_connection.py
# Date: 2025-01-18
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Python database connection testing script

# Importing the create_connection function from db_connection.py
from db_connection import create_connection

# Testing the database connection
if __name__ == "__main__":
    # Call the connection function
    conn = create_connection()
    if conn:
        # If the connection is successful, print and close the connection
        print("Testing connection: Successful!")
        conn.close()
    else:
        # Print a failure message if the connection couldn't be established
        print("Testing connection: Failed!")
