class Human

    attr_accessor :health, :intelligence, :stealth, :strength

    def initialize
        @strength = 3
        @stealth = 3
        @intelligence = 3
        @health = 100
    end

    def attack(opponent)
        if opponent.class.ancestors.include? Human
            opponent.health -= 10

            self
        else
            puts "You cannot attack that"
            self
        end
    end

end

# jason = Human.new

# bosco = Human.new

# jason.attack("bosco")

# puts bosco.health