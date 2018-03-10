require_relative 'bank_account'

RSpec.describe BankAccount do
    before(:each) do
        @bank1 = BankAccount.new
    end

    it 'has a getter method for retreiving the checking account balance' do
        expect(@bank1.show_checking_balance).to eq("You have $0.0 dollars in your checking account.")
    end

    it 'has a getter method that retrieves the total account balance' do
        expect(@bank1.total).to eq(0.0)
    end

    it 'has a function that allows the user to withdraw cash' do
        expect(@bank1.withdraw_from_checking(50)).to eq("You don't have enough money in the checking account!")
    end

    it 'cannot retrieve the total number of bank accounts' do
        expect{@bank1.num_user_accounts}.to raise_error(NoMethodError)
    end

    it 'user cannot set the interest rate' do
        expect{@bank1.interest_rate = 0.5}.to raise_error(NoMethodError)
    end
end