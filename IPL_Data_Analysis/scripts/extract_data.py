# ------------------------------------------------------
# File: extract_data.py
# Date: 2025-01-18
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Extract data from a table in the database

# Import the function to create a database connection from db_connection.py
from db_connection import create_connection

def fetch_table_data(table_name, limit=10):
    """
    Fetches data from a specified table in the database.

    Args:
        table_name (str): The name of the table to fetch data from.
        limit (int): Number of rows to fetch (default is 10).

    Returns:
        list: List of rows retrieved from the table.
    """
    try:
        # Establish the database connection
        conn = create_connection()  # Calls the create_connection function from db_connection.py

        if conn:
            # Create a cursor object to execute SQL queries
            cursor = conn.cursor()

            # Construct the SQL query to fetch a limited number of rows from the table
            query = f"SELECT TOP {limit} * FROM {table_name};"  # Fetches the top 'limit' rows

            # Execute the query
            cursor.execute(query)

            # Fetch all rows returned by the query
            rows = cursor.fetchall()

            # Close the database connection once the data is fetched
            conn.close()

            # Return the fetched rows
            return rows
        else:
            # Print error message if the connection failed
            print("Failed to establish database connection.")
            return None
    except Exception as e:
        # Handle any errors that occur during the execution
        print(f"Error fetching data: {e}")
        return None

# Main block to test the fetch_table_data function
if __name__ == "__main__":
    table_name = "matchsummary"  # Replace with the actual name of the table you want to query
    rows = fetch_table_data(table_name)  # Call the function to fetch data

    if rows:
        # If data was successfully fetched, print it
        print(f"Data from {table_name}:")
        for row in rows:
            print(row)  # Print each row fetched from the table
