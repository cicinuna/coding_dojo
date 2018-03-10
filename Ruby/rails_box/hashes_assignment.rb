# try_one = {:first_key => "First", :second_key => "Second"}
# puts try_one
# puts "Is this #{:first_key} first key and #{:second_key} second key of try_one?"

# try_two = {first_key: "First", second_key: "Second"}
# puts try_two
# puts "Is this #{:first_key} first key and #{:second_key} second key of try_one?"
# puts "What about #{try_two[:first_key]}?"

def new_user greeting="Welcome", first_name: "first", last_name: "last"
    puts "#{greeting}, #{first_name} #{last_name}"      
end
our_user = {first_name: "Jason", last_name: "Shin"}
new_user                  
new_user "Hello", our_user 