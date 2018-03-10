class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        Car.display_all(self)
    
    def display_all(self):
        print "Price: ", self.price
        print "Speed: ", self.speed
        print "Fuel: ", self.fuel
        print "Mileage: ", self.mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        print "Tax: ", self.tax

car1 = Car(2000, "35mph", "Full", "15mpg")
car2 = Car(2000, "5mph", "Full", "105mpg")
car1 = Car(2000, "15mph", "Kind of Full", "95mpg")
car1 = Car(2000, "25mph", "Full", "25mpg")
car1 = Car(2000, "45mph", "Empty", "25mpg")
car1 = Car(20000000, "35mph", "Empty", "15mpg")