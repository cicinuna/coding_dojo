def guess_number guess
  number = 25
  if guess == number
    puts "You Got it!"
  elsif guess < number
    puts "Guess was too low!"
  else
    puts "Guess was too high!"
  end
end

guess_number 25
guess_number 10
guess_number 55