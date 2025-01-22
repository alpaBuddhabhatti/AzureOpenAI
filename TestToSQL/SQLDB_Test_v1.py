import pyodbc
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

print (SERVER)
print (DATABASE)
print (USERNAME)
print(PASSWORD)

DRIVER = 'ODBC Driver 18 for SQL Server'

# Connection string
connection_string = f'DRIVER={{{DRIVER}}};SERVER={SERVER};PORT=1433;DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

# Establishing the connection
try:
    connection = pyodbc.connect(connection_string)
    print("Connection successful")
except Exception as e:
    print(f"Error: {e}")

# Don't forget to close the connection
finally:
    if 'connection' in locals():
        connection.close()
        print("Connection closed")