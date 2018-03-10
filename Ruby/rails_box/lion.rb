require_relative 'mammal'

class Lion < Mammal
    def initialize
        super
        @health += 20
    end

    def fly
        @health -= 10
        self
    end

    def attack_town
        @health -=50
        self
    end

    def eat_humans
        @health += 20
        self
    end

    def show
        puts "This is a lion"
        display_health
    end
end

lion1 = Lion.new.attack_town.attack_town.attack_town.eat_humans.eat_humans.fly.fly.show
