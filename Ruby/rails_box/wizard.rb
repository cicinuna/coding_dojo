require_relative 'human'
class Wizard < Human
    def initialize
        super
        @health -= 50
        @intelligence += 22
    end

    def heal
        @health += 10
        self
    end

    def fireball(opponent)
        if opponent.class.ancestors.include?(Human)
            opponent.health -= 20
            self
        else
            puts "You cannot attack that"
            self
        end
    end


end

# jason = Wizard.new

# puts jason.health
# puts jason.intelligence

# bosco = Human.new

# puts bosco.health
# puts bosco.intelligence

# jason.fireball(bosco)

# puts bosco.health