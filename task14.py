'''14. Cart class
Task: Cart classini yozing.

add_item(name, price) metodida mahsulot qo‘shilsin
get_total() umumiy narxni hisoblasin
'''


class Cart:
    def __init__(self):
        self.items = []   
        
    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def get_total(self):
        return sum(item["price"] for item in self.items)


cart = Cart()
cart.add_item("Laptop", 2000)
cart.add_item("Mouse", 100)
print(cart.get_total())  