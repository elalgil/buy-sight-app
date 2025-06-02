from abc import ABC

from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection

from ebay.Entities.search_request import SearchRequest
from ebay.Entities.site_query_result import SiteQueryResult
from ebay.Entities.site_handler import SiteHandler

CONF_FILE = '../ebay/Entities/ebayconf.yaml'
DOMAIN = 'svcs.sandbox.ebay.com'

SEARCH_BY_KEY_WORD_VERB = 'findItemsByKeywords'


class EbayHandler(SiteHandler, ABC):
    def __init__(self):
        self.connection = Connection(config_file=CONF_FILE, domain=DOMAIN)

    def search_item(self, search_request: SearchRequest) -> SiteQueryResult:
        request_data = {
            'keywords': search_request.get_search_query(),
            'paginationInput': {
                'entriesPerPage': search_request.get_num_results()
            }
        }
        print(request_data)
        try:
            response = self.connection.execute(SEARCH_BY_KEY_WORD_VERB, request_data)
            result = SiteQueryResult()
            try:
                a = response.reply.searchResult.item
            except:
                return result
            print("The result is: " + str(response.reply.searchResult))
            for raw_item in response.reply.searchResult.item:
                result.create_new_item(title=raw_item.title, price=raw_item.sellingStatus.currentPrice.value,
                                       currency=raw_item.sellingStatus.currentPrice._currencyId,
                                       main_image_url=getattr(raw_item, 'galleryURL', None),
                                       condition=getattr(raw_item.condition, 'conditionDisplayName', None),
                                       item_id=raw_item.itemId, product_link=raw_item.viewItemURL)
            return result

        except ConnectionError as e:
            print("Error:", e)
            if e.response:
                print(e.response.dict())
