from openai import OpenAI, api_key, api_type, base_url
import os
from dotenv import load_dotenv

load_dotenv()


openai_api_key = os.getenv('OPENAI_API_KEY')
base_url = os.getenv("BASE_URL")


client = OpenAI(
    base_url=base_url,
    api_key=openai_api_key
)

models = [model.id for model in client.models.list()]

print(models)





