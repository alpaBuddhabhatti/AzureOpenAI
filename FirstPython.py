import os
from openai import AzureOpenAI


# Initialize Azure OpenAI client with key-based authentication
# Please change your AzureOpenAI information
client = AzureOpenAI(
    azure_endpoint = "https://USEYOURAZUREOPENAI.openai.azure.com/",
    api_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    api_version = "XXXXXXXXXXXXXXXXXX",
)
  
completion = client.chat.completions.create(
    model="gpt-40", # This should be your model name
    messages=[{"role": "system", "content": "You are a SQL expert."},
              {"role": "user", "content": "how to improve SQL query performance?"}],
    max_tokens=800,
    temperature=0.7,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0
    )

print(completion.choices[0].message.content)
