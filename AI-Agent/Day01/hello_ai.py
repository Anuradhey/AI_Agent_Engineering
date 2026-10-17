#from openai import OpenAI
#from dotenv import load_dotenv

from openai import OpenAI
from dotenv import load_dotenv

import os

#load config from the .env file
load_dotenv()

#create a client that communicate with Ollama 
client = OpenAI(
    base_url = os.getenv("BASE_URL"),
    api_key = os.getenv("API_KEY")
)

#Send a question to the AI model 
response = client.chat.completions.create(
    model = os.getenv("MODEL"),
    messages=[
        {
         "role": "user",
         "content": "What is 2+2?"
        }
    ]
)

#Display response
print(response.choices[0].message.content)