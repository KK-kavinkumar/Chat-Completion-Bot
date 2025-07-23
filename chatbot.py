
import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()   

clint = AzureOpenAI(
    azure_endpoint =os.getenv("AZURE_OPENAI_API_BASE"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version = "2025-01-01-preview" 
)

response = clint.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "list out the all players in the indian cricket team" }
    ]
)   
print(response.choices[0].message.content)






