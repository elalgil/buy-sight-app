from abc import abstractstaticmethod, abstractmethod


class GeminiRequest:
    def __init__(self, given_prompt: str, response_scheme, mime_type: str = 'text/plain'):
        self._given_prompt = given_prompt
        self._final_prompt = None
        self._response = None
        self._response_scheme = response_scheme
        self._mime_type = mime_type

    @property
    def final_prompt(self):
        return self._final_prompt

    @property
    def mime_type(self):
        return self._mime_type

    @property
    def response_scheme(self):
        return self._response_scheme

    @abstractmethod
    def create_final_prompt(self):
        """
        This function combines between the base prompt from the inherited class and the given prompt from the user.
        :return:
        """
        pass

    def validate_response_schema(self, response: str):
        return True

    def adjust_prompt_if_request_failed(self):
        return True
