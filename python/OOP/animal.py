class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self
    
    def run(self):
        self.health -= 5
        return self
    
    def display_health(self):
        print "This animal currently has: {} health left.".format(self.health)

# dog = Animal("Husky", 100)
# dog.walk().walk().walk().run().run()
# dog.display_health()
# Working as intended

class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

# super_dog = Dog("Husky", 100)
# super_dog.walk().walk().walk().run().run().pet()
# super_dog.display_health()
# Working as intended

class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
        self.health = 170
    
    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a Dragon!"

dog2 = Animal("Chiwa", 50)

# dog2.pet() # gives error
# dog2.fly() # gives error
dog2.display_health() # Does not say "I am a dragon!"

# super_dog.fly() # gives error