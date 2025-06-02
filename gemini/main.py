import json
import os

from dotenv import load_dotenv

from convert_text_to_api_requst import ConvertTextToApiRequest
from gemini import MyGeminiClient

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")


client = MyGeminiClient()
flag = True
inp = input("enter a request: ")
while inp != "quit":
    if flag:
        text_to_api_request = ConvertTextToApiRequest(os.getenv("BASE_PROMPT") + inp)
        flag = False
    else:
        print(os.getenv("SECONDARY_PROMPT") + inp)
        text_to_api_request = ConvertTextToApiRequest(os.getenv("SECONDARY_PROMPT") + inp)
    response = client.request_the_gemini(text_to_api_request)
    print(response)
    inp = input("enter a request: ")
