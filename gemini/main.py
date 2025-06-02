import json
import os

from dotenv import load_dotenv

from convert_text_to_api_requst import ConvertTextToApiRequest
from gemini import MyGeminiClient

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")


client = MyGeminiClient()
text_to_api_request = ConvertTextToApiRequest("Give me please a shopping cart for this prompt: 'i want to have a blue cheap party with bad products that stink'")
response = client.request_the_gemini(text_to_api_request)
print(response)
