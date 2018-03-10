class EventsController < ApplicationController
    def index
			@local_events = Event.where(state: current_user.state)
			@other_events = Event.where.not(state: current_user.state)
		render 'index'
	end

    def create
		if Date.parse(params[:date]).past?
			flash[:errors] = ["Event date must be later than today's Date!"]
          redirect_to :back
        else
          event = Event.new(name: params[:name], date: params[:date], location: params[:location], state: params[:state], user_id: current_user.id)
			if event.save
				flash[:successes] = ["Successfully added an event to the calendar!"]
				redirect_to '/events'
			else
				flash[:errors] = event.errors.full_messages
				redirect_to :back
			end
		end
	end

	def show
		@event = Event.find(params[:id])
		render 'show'
	end
	
	def comment
		comment = Comment.new(content: params[:content], user_id: current_user.id, event_id: params[:id])
		if comment.save
			flash[:successes] = ["Successfully added comment!"]
			redirect_to "/events/#{params[:id]}"
		else
			flash[:errors] = comment.errors.full_messages
			redirect_to :back
		end
	end
end
