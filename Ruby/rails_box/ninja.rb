require_relative 'human'
require_relative 'wizard'
class Ninja < Human
    def initialize
        super
        @stealth += 172
    end

    def get_away
        @health -= 15
        self
    end

    def steal(opponent)
        if opponent.class.ancestors.include?(Human)
            @health += 10
            self
        else
            puts "You cannot steal from that"
            self
        end
    end

end

# jason = Ninja.new

# puts jason.stealth
# puts jason.health

# bosco = Human.new
# eduardo = Wizard.new

# jason.get_away.get_away.steal(bosco).steal(eduardo)

# puts jason.health