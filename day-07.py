"""
Day 07
More classes and objects
"""

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            "name": name,
            "price": price
        })

    def total_price(self):
        return sum([item["price"] for item in self.items])

    @classmethod
    def franchise(cls, store):
        name = "{} - franchise".format(store.name)
        return cls(name)

    @staticmethod
    def store_details(store):
        return "{}, total stock price: {}".format(store.name, int(store.total_price()))



store = Store("Nike Union Square")
store2 = Store("Nike Amazon")

Store.franchise(store)
Store.franchise(store2)

store.add_item("Metcon 4", 160)
store.add_item("Air Max Thea", 95)
store2.add_item("Nike Free RN 2017 Shield", 115)

print(store.store_details(store))
print(store2.store_details(store2))
