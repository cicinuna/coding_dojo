class MathDojo
  # your code here
  attr_reader :num
  def initialize
    @num = 0
  end

  def add(*args)
    # puts *args.inspect
    for things in args
      if things.class == Fixnum
        @num += things
      else
        for nums in things
          @num += nums
        end
      end
    end
    self
  end

  def subtract(*args)
    for things in args
      if things.class == Fixnum
        @num -= things
      else
        for nums in things
          @num -= nums
        end
      end
    end
    self
  end

  def result
    puts @num
    self
  end
end
challenge1 = MathDojo.new.add(2).add(2, 5).subtract(3, 2).result # => 4
challenge2 = MathDojo.new.add(1).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract([2,3], [1.1, 2.3]).result # => 23.15
