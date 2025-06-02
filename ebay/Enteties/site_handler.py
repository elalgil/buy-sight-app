from abc import ABC, abstractmethod
from ebay.Entities.search_request import SearchRequest
from ebay.Entities.search_result import SearchResult


class SiteHandler(ABC):
    """
    Represents a handler working with a specific shopping site.
    """
    @abstractmethod
    def search_item(self, search_request: SearchRequest) -> SearchResult:
        """
        Searches an item on the site and returns results.
        :param search_request:
        :return:
        """
        pass


