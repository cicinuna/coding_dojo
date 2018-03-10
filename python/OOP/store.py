import product

class Store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner

    def add_product(self, new_product):
        self.products = self.products.append(new_product)
        return self

    def remove_product(self, name):
        pass

    def inventory(self):
        for i in range(0, len(self.products)):
            print self.products[i]
        print self.owner
        print self.location


item1 = product.Product(30, "Onion", "2lbs", "organic", 20, "for sale")
item2 = product.Product(15, "Grape", "4lbs", "organic", 5, "for sale")
item3 = product.Product(45, "Rice", "15lbs", "Korea", 20, "for sale")
item4 = product.Product(5, "Candy", "0.3lbs", "Junk", 1, "for sale")
item5 = product.Product(7, "Scallion", "0.5lbs", "organic", 2, "for sale")

store1 = Store([item1, item2, item3, item4, item5], "Coding Dojo, Burbank CA 99999", "Jason Shin")

Store.inventory(store1)

