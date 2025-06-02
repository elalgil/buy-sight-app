from typing import *
from ebay.Entities.item import Item


class SearchResult:
    """
    This class creates Item objects from the data received from the ecommerce API.
    every new item created is added to items list
    """

    def __init__(self):
        self._items: List[Item] = []

    def create_new_item(self, item_id: str, title: str, price: float,
                        condition: str,
                        main_image_url: str, product_link: str, currency: str):
        """
        This func receive all required fields to create a new Item object and
        add this new item to search result Items
        :param currency: product price currency
        :param item_id: item id from ecommerce site
        :param title: item product title
        :param price: product price
        :param condition: product condition
        :param main_image_url: item's main image from ecommerce site
        :param product_link: purchase link to this product from ecommerce site
        :return:
        """
        new_item: Item = Item(item_id, title, price, condition, main_image_url,
                              product_link, currency)
        self._items.append(new_item)

    def get_items(self):
        return self._items
