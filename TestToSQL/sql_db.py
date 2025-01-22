# sql_db_azure.py

import pyodbc
import pandas as pd
import os
from dotenv import load_dotenv 
import requests


DRIVER = 'ODBC Driver 18 for SQL Server'

# Load environment variables from .env file
load_dotenv()
# Get the Azure OpenAI key and endpoint from the environment variables
SERVER = os.getenv("SERVER")
DATABASE = os.getenv("DATABASE")
USERNAME = os.getenv("DBUSERNAME")
PASSWORD = os.getenv("PASSWORD")
# Connection string
connection_string = f'DRIVER={{{DRIVER}}};SERVER={SERVER};PORT=1433;DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'


def create_connection():
    """ Create or connect to an Azure SQL database """
    try:
        # Establish a connection to the Azure SQL Database
        conn = pyodbc.connect(connection_string)
        return conn
    except pyodbc.Error as e:
        # Print the error if connection fails
        print(f"Error connecting to database: {e}")
        return None  # Return None if there's a connection error

def query_database(query):
    """ Run SQL query and return results in a dataframe """
    conn = create_connection()
    if conn:
        try:
            # Execute the query and return the results in a dataframe
            df = pd.read_sql_query(query, conn)
            return df
        except Exception as e:
            # Print the error if query execution fails
            print(f"Error executing query: {e}")
            return None
        finally:
            # Ensure the connection is closed after the query execution
            conn.close()
    else:
        print("Failed to connect to the database.")
        return None

def get_schema_representation():
    """ Get the database schema in a JSON-like format """
    conn = create_connection()
    if not conn:
        print("Failed to connect to the database.")
        return None

    cursor = conn.cursor()

    # Query to get all table names
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_type = 'BASE TABLE';")
    tables = cursor.fetchall()

    db_schema = {}

    for table in tables:
        table_name = table[0]

        # Query to get column details for each table
        cursor.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table_name}';")
        columns = cursor.fetchall()

        column_details = {column[0]: column[1] for column in columns}
        db_schema[table_name] = column_details

    conn.close()
    return db_schema

# This will query the database and get the schema when you run sql_db_azure.py
if __name__ == "__main__":
    # Example query to get data from an existing table
    query = "SELECT * FROM Orders"  # Modify this to query an existing table in your Azure SQL DB
    result_df = query_database(query)
    if result_df is not None:
        print(result_df)

    # Getting the schema representation
    schema = get_schema_representation()
    if schema:
        print(schema)