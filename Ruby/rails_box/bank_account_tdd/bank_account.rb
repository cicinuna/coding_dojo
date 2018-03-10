class BankAccount
    @@prng = Random.new
    @@num_user_accounts = 0
    @@interest_rate = 0.01
    def initialize
        @saving = @@prng.rand(1000000...9999999)
        @checking = @@prng.rand(1000000...9999999)
        @saving_balance = 0.0
        @checking_balance = 0.0
        @total_fund = 0.0
        @@num_user_accounts += 1
    end

    def total
        @total_fund
    end

    def show_saving_balance
        puts "You have $#{@saving_balance} dollars in your savings account."
        self
    end

    def show_checking_balance
        "You have $#{@checking_balance} dollars in your checking account."
    end

    def deposit_to_saving(add)
        @saving_balance += add
        @total_fund += add
        puts "You have deposited $#{add} to the savings account!"
        self
    end

    def deposit_to_checking(add)
        @checking_balance += add
        @total_fund += add
        puts "You have deposited $#{add} to the checking account!"
        self
    end

    def withdraw_from_saving(subtract)
        if @saving_balance < subtract
            puts "You don't have enough money in the savings account!"
            self
        else
            @saving_balance -= subtract
            @total_fund -= subtract
            puts "You have withdrawn $#{subtract} from the savings account!"
            self
        end
    end

    def withdraw_from_checking(subtract)
        if @checking_balance < subtract
            "You don't have enough money in the checking account!"
        else
            @checking_balance -= subtract
            @total_fund -= subtract
            puts "You have withdrawn $#{subtract} from the checking account!"
            self
        end
    end

    def account_information
        puts "Your Savings Account Number is: #{@saving}."
        puts "Your Checking Account Number is: #{@checking}."
        puts "You have $#{@saving_balance} in your Savings Account."
        puts "You have $#{@checking_balance} in your Checking Account."
        puts "You have $#{@total_fund} total with our bank."
        puts "Our bank's interest rate with you is #{@@interest_rate}."
    end

    def self.show_how_many_accounts
        puts "Bank has #{@@num_user_accounts} accounts currently."
    end
end

account1 = BankAccount.new

account1.deposit_to_checking(5000.0).deposit_to_saving(15000.0).withdraw_from_checking(500.0).account_information

account2 = BankAccount.new

account2.deposit_to_checking(120.0).withdraw_from_checking(70.0).account_information

BankAccount.show_how_many_accounts