class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayInfo(self):
        print "Price: ", self.price
        print "Max Speed: ", self.max_speed
        print "Current Milage: ", self.miles
        # return self

    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing"
        self.miles -= 5
        return self
        # You could have checks here to do something like:
        # If self.miles is between 0 and 4 inclusive
        # Output a message saying soemthing like You can't reverse
        # else go ahead and do reverse


bike1 = Bike(250,"30mph")
bike2 = Bike(400,"40mph")
bike3 = Bike(1200, "45mph")

# Bike.ride(bike1)
# Bike.ride(bike1)
# Bike.ride(bike1)
# Bike.reverse(bike1)
# Bike.displayInfo(bike1)

# Bike.ride(bike1).ride(bike1).ride(bike1).reverse(bike1).displayInfo(bike1)
Bike.displayInfo(Bike.reverse(Bike.ride(Bike.ride(Bike.ride(bike1)))))

Bike.ride(bike2)
Bike.ride(bike2)
Bike.reverse(bike2)
Bike.reverse(bike2)
Bike.displayInfo(bike2)

Bike.reverse(bike3)
Bike.reverse(bike3)
Bike.reverse(bike3)
Bike.displayInfo(bike3)
