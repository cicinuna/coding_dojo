require_relative 'project'

RSpec.describe Project do
    before(:each) do
        @project1 = Project.new('Project1', 'description 1', "John Doe")
        @project2 = Project.new('Project2', 'description 2', "John Doe")
    end

    it 'has a getter and setter for name and description' do
        @project1.name = 'Some other project name'
        expect(@project1.name).to eq('Some other project name')
    end

    it 'has a method elevator_pitch to explain name and description' do
        expect(@project1.elevator_pitch).to eq('Project1, description 1')
        expect(@project2.elevator_pitch).to eq('Project2, description 2')
    end

    it 'has a getter and setter for owner attribute' do
        @project1.owner = "Jane Doe"
        expect(@project1.owner).to eq("Jane Doe")
    end

    it 'has a method tasks to return all tasks for each project object' do
        expect(@project1.tasks).to eq([])
        expect(@project2.tasks).to eq([])
    end

    it 'has a method add_tasks to add tasks for each project object' do
        expect(@project1.add_tasks('do this and that')).to eq(['do this and that'])
        expect(@project2.add_tasks('do that and this')).to eq(['do that and this'])
    end
end
