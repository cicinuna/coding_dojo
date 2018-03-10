class Apple
    attr_accessor :age
    attr_reader :height, :apples

    def initialize
        @age = 1
        @height = 1.0
        @apples = 0
    end

    def year_gone_by
        @age += 1
        @height += @height / 10
        if @age > 3 && @age < 11
            @apples += 2
        end
    end

    def pick_apples
        @apples = 0
    end
end