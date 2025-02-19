import os
from openai import AzureOpenAI

from dotenv import load_dotenv 
import requests


# Load environment variables from .env file
load_dotenv()
# Get the Azure OpenAI key and endpoint from the environment variables
api_key = os.getenv("AZURE_OPENAI_KEY")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
#pip install requests
print(api_key)
print(endpoint)
# Initialize Azure OpenAI client with key-based authentication
client = AzureOpenAI(
   # azure_endpoint = "https://azureopenai24demo.openai.azure.com/",
   # api_key = "7c15f7bb4139435bbefa4b8e155a1622",
   api_key = api_key ,
   azure_endpoint = endpoint,
    api_version = "2024-05-01-preview",
)
  
completion = client.chat.completions.create(
    model="gpt-40",
    messages=[{"role": "system", "content": "You are a SQL expert."},
              {"role": "user", "content": "how to improve SQL query performance?"}],
    max_tokens=800,
    temperature=0.7,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0
    )

print(completion.choices[0].message.content) 


