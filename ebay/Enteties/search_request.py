from typing import *


class SearchRequest:
    """
    This class is immutable, it creates a search request object which contain
    a title of the product requested to search in site and all the search
    preferences received from user.
    @:param preferences is a generic dictionary created by the site handler.
    """

    def __init__(self, title: str, preferences: Dict[str, str],
                 num_results: int, query: str):
        """
        :param title: item product search title
        :param preferences: dictionary of pref: pref_description from user, for this search
        :param num_results: number of result to request from ecommerce API for this requested item
        """
        self._title: str = title
        self._preferences: Dict[str, str] = preferences
        self._num_results = num_results
        self._query = query

    def add_preference(self, pref: str, description: str):
        if pref not in self._preferences:
            self._preferences[pref] = description
        else:
            raise ValueError(
                f"Key: {pref} already inserted to Preferences dict")

    def change_pref_value(self, pref: str, new_desc: str):
        if pref not in self._preferences:
            raise ValueError(f"Key {pref} does not exist in Preferences dict")
        else:
            self._preferences[pref] = new_desc

    def get_title(self):
        return self._title

    def get_preferences(self):
        return self._preferences

    def get_num_results(self):
        return self._num_results

    def get_search_query(self):
        return self._query

    def set_num_results(self, num_results: int):
        self._num_results = num_results
