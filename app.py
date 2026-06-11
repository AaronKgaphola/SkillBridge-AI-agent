import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    base_url=f"{os.getenv('AZURE_OPENAI_ENDPOINT')}/openai/v1/"
)

def ask_skillbridge(prompt):
    response = client.responses.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        input=prompt
    )

    return response.output_text

answer = ask_skillbridge(
    "Recommend career paths for a student interested in Python and AI."
)

print(answer)
