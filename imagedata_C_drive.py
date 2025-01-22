import os
import base64
from openai import AzureOpenAI

# Set the directory to C drive test folder
os.chdir(r"C:\Users\XXX\XXX\test")

# Initialize Azure OpenAI client with key-based authentication
client = AzureOpenAI(
    azure_endpoint = "https://USEYOURAZUREOPENAI.openai.azure.com/",
    api_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    api_version = "XXXXXXXXXXXXXXXXXX",
)
  


# Set image path using raw string to avoid escape sequence issues
image_path = r"C:\Users\XXX\XXX\XX\house.jpeg"

# Convert image to base64
with open(image_path, "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode("utf-8")

# Use base64 encoded data URL
#change jpeg to other image type if you have image with other then jpeg
image_data_url = f"data:image/jpeg;base64,{base64_image}"

completion = client.chat.completions.create(
    model="gpt-40", #Your Model name
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": image_data_url,
                    }
                },
            ],
        }
    ],
    max_tokens=300,
)

print(completion.model_dump_json(indent=2))
