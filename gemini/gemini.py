import os
import json
from dotenv import load_dotenv
from google import genai

from gemini_request import GeminiRequest

load_dotenv()


class MyGeminiClient:
    def __init__(self, model: str = "gemini-2.0-flash", max_output_tokens=500):
        self._model = model
        self._max_output_tokens = max_output_tokens
        self._client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))



    def request_the_gemini(self, gemini_request: GeminiRequest):
        """
        this function actually asks the gemini.
        :return: gemini's response as a json string
        """

        tmp_response = self._client.models.generate_content(
            model=self._model,
            contents=gemini_request.final_prompt,
            config={'response_mime_type': gemini_request.mime_type,
                    'response_schema':gemini_request.response_scheme,}
        )

        while True:
            if not gemini_request.validate_response_schema(json.loads(tmp_response.text)):
                if gemini_request.adjust_prompt_if_request_failed():
                    #  False iff when there were too many tryings to fix
                    tmp_response = self._client.models.generate_content(
                        model=self._model,
                        contents=gemini_request.final_prompt,
                        config={'response_mime_type': gemini_request.mime_type})
                else:
                    return False # todo should raise a message of HALAS
            else:
                break

        return tmp_response.text