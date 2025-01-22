from dotenv import load_dotenv
import os
import openai
from openai import AzureOpenAI

load_dotenv()



client = AzureOpenAI(
  azure_endpoint = "https://azureopenai24demo.openai.azure.com/", 
  api_key="7c15f7bb4139435bbefa4b8e155a1622",
  api_version="2024-05-01-preview"
)


def get_completion_from_messages(system_message, user_message, model="gpt-40", temperature=0, max_tokens=500) -> str:

    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': f"{user_message}"}
    ]
    
    print("user message:  ", user_message)
   
    
    response =  client.chat.completions.create(
        #engine=model,
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens, 
    )
    
    return response.choices[0].message.content


if __name__ == "__main__":
    system_message = "You are a helpful assistant"
    user_message = "Hello, how are you?"
    print(get_completion_from_messages(system_message, user_message))