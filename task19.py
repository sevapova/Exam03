'''19. Mixins
Task: JsonMixin obyektni JSON ga aylantirsin.
'''

import json

class JsonMixin:
    def to_json(self):
        return json.dumps(self.__dict__)


class Product(JsonMixin):
    def __init__(self, name, price):
        self.name = name
        self.price = price


product = Product("Laptop", 1500)
print(product.to_json())




