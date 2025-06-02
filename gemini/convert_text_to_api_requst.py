import json
import os

from dotenv import load_dotenv
from jsonschema import validate, ValidationError

from gemini_request import GeminiRequest


class ConvertTextToApiRequest(GeminiRequest):
    load_dotenv()

    allowed_trys = int(os.getenv("MAX_ALLOWED_API_CALLS_TRYS"))
    base_prompt = ''

    # load the scheme from .env
    with open(os.getenv("RESPONSE_SCHEME_PATH")) as sf:
        response_scheme = json.load(sf)

    def __init__(self, given_prompt: str, mime_type: str = "application/json"):
        super().__init__(given_prompt, ConvertTextToApiRequest.response_scheme, mime_type)
        self._final_prompt = self.create_final_prompt()

    def adjust_prompt_if_request_failed(self):
        """
        used when the response, which converts the Free Text into JSON (to API request), doesn't fit the scheme.
        we therefore need to ask gemini to fix itself
        """
        if ConvertTextToApiRequest.allowed_trys == 0:
            return False  # announce that HALAS
        ConvertTextToApiRequest.allowed_trys -= 1
        self._final_prompt += "\nPlease follow the Scheme guidelines"
        self._final_prompt += "!" * (
                    int(os.getenv("MAX_ALLOWED_API_CALLS_TRYS")) - ConvertTextToApiRequest.allowed_trys)
        return True

    def create_final_prompt(self) -> str:
        return ConvertTextToApiRequest.base_prompt + self._given_prompt

    def validate_response_schema(self, response):
        """
        compare the response for this request to a given json schema
        # :param schema_path: file path to the schema
        :return: True if the response matches the schema, False otherwise
        """
        # with open(ConvertTextToApiRequest.response_scheme, 'r') as schema_file:
        #     schema = json.load(schema_file)

        try:
            validate(instance=response, schema=ConvertTextToApiRequest.response_scheme)
            return True

        except ValidationError as e:
            print("Invalid response schema")
            print(e.message)
            return False
