from ebaysdk.finding import Connection
from ebaysdk.exception import ConnectionError

from ebay.Entities.ebay_handler import EbayHandler
from ebay.Entities.search_request import SearchRequest


# EXAMPLE CODE
def example():
    try:
        # Create API connection using config file (sandbox or production)
        api = Connection(config_file='Entities/ebayconf.yaml',
                         domain='svcs.sandbox.ebay.com')

        # Execute search by keyword
        response = api.execute('findItemsByKeywords', {
            'keywords': 'iphone',
            'itemFilter': [{"name": "MinPrice",
                            "value": '70'}, {"name": "MaxPrice",
                                             "value": '700'}],
            'paginationInput': {
                'entriesPerPage': 5
            }
        })

        # Loop through the search results
        for item in response.reply.searchResult.item:
            title = item.title
            price = item.sellingStatus.currentPrice.value
            currency = item.sellingStatus.currentPrice._currencyId
            print(f"{title} - {price} {currency}")

    except ConnectionError as e:
        print("Error:", e)
        if e.response:
            print(e.response.dict())


if __name__ == '__main__':
    handler = EbayHandler()
    mock_request = SearchRequest(title='computer', query='laptop',
                                 num_results=5, preferences={"MinPrice": "30",
                                                             "MaxPrice": "300"})
    result = handler.search_item(mock_request)
    for item in result.get_items():
        print(
            f'title: {item.get_title()}\nprice:{item.get_price()}\ncolor:{item.get_color()}\nitem ID:{item.get_item_id()}\n\n')
