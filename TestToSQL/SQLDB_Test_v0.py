import pyodbc

# Connection details for Azure SQL Database
SERVER = 'azureopenai24databaseserverdemo.database.windows.net'
DATABASE = 'azureopenaidemo'
USERNAME = 'Alpa'
PASSWORD = 'Shivam123?'
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