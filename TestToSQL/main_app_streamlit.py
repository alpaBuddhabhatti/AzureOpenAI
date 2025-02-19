import streamlit as st
import pandas as pd
import sql_db
from prompts.prompts import SYSTEM_MESSAGE
from azure_openai import get_completion_from_messages
import json

def query_database(query, conn):
    """ Run SQL query and return results in a dataframe """
    return pd.read_sql_query(query, conn)

# Create or connect to SQLite database
conn = sql_db.create_connection()

# Schema Representation for multiple tables
schemas = sql_db.get_schema_representation()
print(schemas)

st.title("SQL Query Generator with gpt-40")
st.write("Enter your message to generate SQL and view results.")

# Input field for the user to type a message
user_message = st.text_input("Enter your message:")

if user_message:
    # Format the system message with the schema
    formatted_system_message = SYSTEM_MESSAGE.format(schema=schemas)
    print("formatted_system_message:", formatted_system_message)

    # Use gpt-35-turbo to generate the SQL query
    response = get_completion_from_messages(formatted_system_message, user_message)
    print("Azure Open AI response: ", response)

    # Clean the response by removing the code block formatting
    cleaned_response = response.strip().replace('```json', '').replace('```', '').strip()

    try:
        json_response = json.loads(cleaned_response)
        query = json_response['query']

        # Display the generated SQL query
        st.write("Generated SQL Query:")
        st.code(query, language="sql")

        # Run the SQL query and display the results
        sql_results = query_database(query, conn)
        st.write("Query Results:")
        st.dataframe(sql_results)

    except json.JSONDecodeError as e:
        st.write("Failed to decode JSON:", e)
    except KeyError as e:
        st.write(f"Key not found in JSON response: {e}")
    except Exception as e:
        st.write(f"An error occurred: {e}")
