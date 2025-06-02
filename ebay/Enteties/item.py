class Item:
    """
    Class contain all the basic information about a specific product received
    from the Ebay API using Finding Library. Each field can be changed using
    getters and setters.
    """

    def __init__(self, item_id: str, title: str, price: float, condition: str,
                 main_image_url: str, product_link: str, currency: str):
        self._item_id = item_id
        self._title = title
        self._price = price
        self._currency = currency
        self._condition = condition
        self._main_image_url = main_image_url
        self._additional_images = []
        self._product_link = product_link

        # additional fields:
        self._color = None
        self._category_id = None
        self._category_name = None
        self._shipping_cost = None
        self._scale_info = None

    def get_item_id(self):
        return self._item_id

    def set_item_id(self, item_id):
        self._item_id = item_id

    # title
    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    # price
    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    # condition
    def get_condition(self):
        return self._condition

    def set_condition(self, condition):
        self._condition = condition

    # main_image_url
    def get_main_image_url(self):
        return self._main_image_url

    def set_main_image_url(self, url):
        self._main_image_url = url

    # additional_images
    def get_additional_images(self):
        return self._additional_images

    def set_additional_images(self, images):
        self._additional_images = images

    def add_image(self, image_url: str):
        self._additional_images.append(image_url)

    # product_link
    def get_product_link(self):
        return self._product_link

    def set_product_link(self, link):
        self._product_link = link

    # color
    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    # category_id
    def get_category_id(self):
        return self._category_id

    def set_category_id(self, category_id):
        self._category_id = category_id

    # category_name
    def get_category_name(self):
        return self._category_name

    def set_category_name(self, category_name):
        self._category_name = category_name

    # shipping_cost
    def get_shipping_cost(self):
        return self._shipping_cost

    def set_shipping_cost(self, cost):
        self._shipping_cost = cost

    # scale_info
    def get_scale_info(self):
        return self._scale_info

    def set_scale_info(self, info):
        self._scale_info = info

    def to_dict(self):
        """This func convert all Item instance fields into a jason format"""
        return {
            "item_id": self._item_id,
            "title": self._title,
            "price": self._price,
            "currency": self._currency,
            "condition": self._condition,
            "main_image_url": self._main_image_url,
            "additional_images": self._additional_images,
            "product_link": self._product_link
        }
