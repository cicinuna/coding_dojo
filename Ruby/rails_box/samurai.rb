require_relative 'human'
require_relative 'wizard'
require_relative 'ninja'

class Samurai < Human
    @@samurai_count = 0
    def initialize
        super
        @health += 100
        @@samurai_count += 1
    end

    def meditate
        @health = 200
        self
    end

    def death_blow(opponent)
        if opponent.class.ancestors.include?(Human)
            opponent.health = 0
            self
        else
            puts "You cannot apply lethal blow to that thing"
            self
        end
    end

    def self.how_many
        puts "There are #{@@samurai_count} samurais total!"
    end

end

jason = Samurai.new
bosco = Samurai.new
eduardo = Samurai.new

nick = Human.new
nate = Human.new
kevin = Wizard.new

kevin.fireball(jason)

puts jason.health
jason.meditate
puts jason.health

jason.death_blow(kevin)

puts kevin.health

Samurai.how_many