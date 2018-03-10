class Product(object):
    def __init__(self, price, name, weight, brand, cost, status):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status
    
    def sell(self):
        self.status = "Sold"
        return self

    def add_tax(self, tax):
        self.price = self.price + (self.price * tax)
        return self

    def return_item(self, reason):
        if reason == "defective":
            self.status = reason
            self.price = 0
        else:
            if reason == "opened":
                self.status = "used"
                self.price = self.price - (self.price * 0.20)
            elif reason == "unopened":
                self.status = "for sale"
        return self

    def display_info(self):
        print "The Item's name is : ", self.name
        print "The Item's price is : ", self.price
        print "The Item's weight is : ", self.weight
        print "The Item's brand is : ", self.brand
        print "The Item's cost is : ", self.cost
        print "The Item's status is : ", self.status

class Store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner

    def add_product(self, new_product):
        self.products = self.products.append(new_product)
        print self.products
        return self

    def remove_product(self, name):
        pass

    def inventory(self):
        for i in range(0, len(self.products)):
            print Product.display_info(self.products[i])
        print self.owner
        print self.location

item1 = Product(30, "Onion", "2lbs", "organic", 20, "for sale")
item2 = Product(15, "Grape", "4lbs", "organic", 5, "for sale")
item3 = Product(45, "Rice", "15lbs", "Korea", 20, "for sale")
item4 = Product(5, "Candy", "0.3lbs", "Junk", 1, "for sale")
item5 = Product(7, "Scallion", "0.5lbs", "organic", 2, "for sale")

# print item1

# Product.display_info(item1)
# Product.display_info(item2)
# Product.display_info(item3)
# Product.display_info(item4)
# Product.display_info(item5)

# Product.add_tax(item1, 0.1)
# Product.add_tax(item2, 0.1)
# Product.add_tax(item3, 0.1)
# Product.add_tax(item4, 0.1)
# Product.add_tax(item5, 0.1)

# print "After adding tax: "

# Product.display_info(item1)
# Product.display_info(item2)
# Product.display_info(item3)
# Product.display_info(item4)
# Product.display_info(item5)

# print "Returning a used onion: "
# print " "

# Product.display_info(Product.return_item(item1, "opened"))

# print "Returning a defective grape: "
# print " "
# Product.display_info(Product.return_item(item2, "defective"))

# print "Returning a perfectly fine Rice: "
# print " "
# Product.display_info(Product.return_item(item3, "unopened"))

# Everything working as intended!!




store1 = Store([item1, item2, item3, item4, item5], "Coding Dojo, Burbank CA 99999", "Jason Shin")

# Store.inventory(store1)

item6 = Product(500, "Model Plane", "10lbs", "toys", 220, "for sale")
Store.add_product(store1, item6)

Store.inventory(store1)
