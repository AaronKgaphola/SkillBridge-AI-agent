import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    base_url=f"{os.getenv('AZURE_OPENAI_ENDPOINT')}/openai/v1/"
)

response = client.responses.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    input="What model are you?"
)

print(response.output_text)