from typing import *
from ebay.Entities.item import *


class SearchMatches:
    def __init__(self):
        self._matches: Dict[str, List[Item]] = {}

    def insert_item_list(self, title: str, item_lst: List[Item]):
        if title not in self._matches:
            self._matches[title] = item_lst
        else:
            raise ValueError(
                f"title {title} already in SearchResult dictionary")

    def get_item_lst(self, title: str):
        """Func receive a title and return the mathing item list with this title"""
        if title not in self._matches:
            raise KeyError(f"Title: {title} not in SearchMatches dictionary")
        else:
            return self._matches[title]

    def get_matches(self):
        return self._matches
