import os
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

endpoint = os.getenv("ENDPOINT_URL", "https://azureventureopenaieastus.openai.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-35-turbo-16k")
search_endpoint = os.getenv("SEARCH_ENDPOINT", "https://venturepocazureaisearch1.search.windows.net")
search_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"#os.getenv("SEARCH_KEY", "put your Azure AI Search admin key here")
search_index = os.getenv("SEARCH_INDEX_NAME", "index")

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default")
      
client = AzureOpenAI(
    azure_endpoint=endpoint,
    #azure_ad_token_provider=token_provider,
    api_key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    api_version="2024-05-01-preview",
)
      
completion = client.chat.completions.create(
    model=deployment,
    messages= [
    {
      "role": "user",
      "content": "top 2 coversation having issues"
    }],
    max_tokens=800,
    temperature=0,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    stream=False,
    extra_body={
      "data_sources": [{
          "type": "azure_search",
          "parameters": {
            "endpoint": f"{search_endpoint}",
            "index_name": "index",
            "semantic_configuration": "default",
            "query_type": "semantic",
            "fields_mapping": {},
            "in_scope": True,
            "role_information": "You are an AI assistant that helps people find information.",
            "filter": None,
            "strictness": 3,
            "top_n_documents": 5,
            "authentication": {
              "type": "api_key",
              "key": f"{search_key}"
            }
          }
        }]
    }
)
print(completion.to_json())