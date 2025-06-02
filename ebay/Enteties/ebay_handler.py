from abc import ABC

from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection

from ebay.Entities.search_request import SearchRequest
from ebay.Entities.site_query_result import SiteQueryResult
from ebay.Entities.site_handler import SiteHandler

CONF_FILE = '../ebay/Entities/ebayconf.yaml'
DOMAIN = 'svcs.sandbox.ebay.com'
REAL_DOMAIN = 'svcs.ebay.com'

SEARCH_BY_KEY_WORD_VERB = 'findItemsByKeywords'


class EbayHandler(SiteHandler, ABC):
    def __init__(self):
        self.connection = Connection(config_file=CONF_FILE, domain=DOMAIN)

    def search_item(self, search_request: SearchRequest) -> SiteQueryResult:
        request_data = {
            'keywords': search_request.get_search_query(),
            'itemFilter': [{"name": "MinPrice",
                            "value": search_request.get_preferences().get(
                                "MinPrice")}, {"name": "MaxPrice",
                                               "value": search_request.get_preferences().get(
                                                   "MaxPrice")}],
            'paginationInput': {
                'entriesPerPage': search_request.get_num_results()
            }
        }
        print("Sending request to eBay with data:", request_data)

        result = SiteQueryResult()  # Always return this, even on failure

        try:
            response = self.connection.execute(SEARCH_BY_KEY_WORD_VERB,
                                               request_data)
            ack = getattr(response.reply, 'ack', None)
            print("Response ACK:", ack)

            search_result = getattr(response.reply, 'searchResult', None)
            if not search_result or int(
                    getattr(search_result, '_count', 0)) == 0:
                print("No items found.")
                return result

            items = getattr(search_result, 'item', [])
            if not isinstance(items, list):
                items = [items]  # normalize single item

            for raw_item in items:
                result.create_new_item(
                    title=raw_item.title,
                    price=raw_item.sellingStatus.currentPrice.value,
                    currency=raw_item.sellingStatus.currentPrice._currencyId,
                    main_image_url=getattr(raw_item, 'galleryURL', None),
                    condition=getattr(raw_item.condition,
                                      'conditionDisplayName', None),
                    item_id=raw_item.itemId,
                    product_link=raw_item.viewItemURL
                )
            return result

        except ConnectionError as e:
            print("ConnectionError occurred while querying eBay API.")
            print("Error:", str(e))
            if e.response:
                try:
                    print("Error response:", e.response.dict())
                    print("Response headers:", e.response.response.headers)
                except Exception as ex:
                    print("Could not parse error response:", str(ex))
            return result
