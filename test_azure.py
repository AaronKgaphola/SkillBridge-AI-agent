import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
print("ENDPOINT =", repr(os.getenv("AZURE_OPENAI_ENDPOINT")))
print("KEY EXISTS =", bool(os.getenv("AZURE_OPENAI_KEY")))
print("DEPLOYMENT =", repr(os.getenv("AZURE_OPENAI_DEPLOYMENT")))
client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    base_url=f"{os.getenv('AZURE_OPENAI_ENDPOINT')}/openai/v1/"
)

response = client.responses.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    input="Say hello"
)

print(response.output_text)