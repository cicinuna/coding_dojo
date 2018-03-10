require_relative 'mammal'

class Dog < Mammal
    def pet
        @health += 5
        self
    end

    def walk
        @health -= 1
        self
    end

    def run
        @health -= 10
        self
    end

    def show_health
        self.display_health
    end

end

dog1 = Dog.new.walk.walk.walk.run.run.pet.show_health