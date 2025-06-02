import json
from typing import *

import ebay.Entities.ebay_handler
from ebay.Entities.search_matches import SearchMatches
from ebay.Entities.search_request import SearchRequest
from ebay.Entities.site_handler import SiteHandler
from gemini.convert_text_to_api_requst import ConvertTextToApiRequest
from gemini.gemini import MyGeminiClient

NUM_RESULTS = 5  # by default num results is 1


def initialize_ebay_handler():
    return ebay.Entities.ebay_handler.EbayHandler()


class AppLogic:
    def __init__(self):
        self.site_handlers: list[SiteHandler] = [initialize_ebay_handler()]
        self.gemini_client = MyGeminiClient()

    def search_items(self, free_text: str) -> SearchMatches:
        """
        Searches all sites for items requested by user.
        :param free_text: Free text description
        :return:
        """
        search_requests = self.free_text_to_search_requests(free_text)
        matches = SearchMatches()
        for req in search_requests:  # For every item we want
            item_results = []
            for handler in self.site_handlers:  # Search every site
                item_results += handler.search_item(req).get_items()  # Add results to list
            matches.insert_item_list(req.get_title(), item_results)  # Insert item list to search_matches
        return matches

    def make_search_request_from_json(self, json_str):
        try:
            raw_items = json.loads(json_str)
            search_requests: List[SearchRequest] = []

            for item in raw_items:
                title = item.get("title", "")
                query = item.get("query", "")
                preferences: Dict[str, Any] = {}

                # Insert all other fields into preferences as-is
                for key, value in item.items():
                    if key not in ("title", "query"):
                        preferences[key] = value

                search_request = SearchRequest(
                    title=title,
                    preferences=preferences,
                    num_results=NUM_RESULTS,
                    query=query
                )
                search_requests.append(search_request)

            return search_requests

        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON: {e}")
            return []

    def free_text_to_search_requests(self, free_text: str) -> list[SearchRequest]:
        text_to_api_request = ConvertTextToApiRequest(free_text)
        return self.make_search_request_from_json(self.gemini_client.request_the_gemini(text_to_api_request))
