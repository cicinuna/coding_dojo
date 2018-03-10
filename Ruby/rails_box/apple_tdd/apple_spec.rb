require_relative 'apple'

RSpec.describe Apple do
    before(:each) do
        @apple = Apple.new
    end

    it 'has getter and setter for age attribute' do
        @apple.age = 5
        expect(@apple.age).to eq(5)
    end

    it 'has getter method only for height attribute' do
        expect(@apple.height).to eq(1.0)
        expect{@apple.height = 5}.to raise_error(NoMethodError)
    end

    it 'has getter method only for apples attribute' do
        expect(@apple.apples).to eq(0)
        expect{@apple.apples = 10}.to raise_error(NoMethodError)
    end

    it 'has a method year_gone_by that adds 1 year to age, increase height by 10% and raise apple count by two given appropriate age' do
        @apple.year_gone_by
        expect(@apple.age).to eq(2)
        expect(@apple.height).to eq(1.1)
        expect(@apple.apples).to eq(0)
    end

    it 'cannot grow apples for the first three years of life' do
        @apple.age = 2
        expect(@apple.apples).to eq(0)
    end

    it 'has pick_apples method that takes all apples from tree' do
        @apple.pick_apples
        expect(@apple.apples).to eq(0)
    end

end