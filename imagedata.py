

import os
from openai import AzureOpenAI


# Initialize Azure OpenAI client with key-based authentication
client = AzureOpenAI(
    azure_endpoint = "https://USEYOURAZUREOPENAI.openai.azure.com/",
    api_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    api_version = "XXXXXXXXXXXXXXXXXX",
)
  
completion = client.chat.completions.create(
    model="gpt-40", # This should be your model name

    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://raw.githubusercontent.com/MicrosoftDocs/azure-ai-docs/main/articles/ai-services/openai/media/how-to/generated-seattle.png",
                    }
                },
            ],
        }
    ],
    max_tokens=300,
)

print(completion.model_dump_json(indent=2))
