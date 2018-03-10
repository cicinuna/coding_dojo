class WallsController < ApplicationController
	def new
		render 'new'
	end

	def process_user
		@user = User.find_by(username: params[:username])
		puts @user.username
		puts @user.id
		if @user == nil
			User.create(username: params[:username])
			session[:id] = User.last.id
			redirect_to '/messages'
		else
			session[:id] = @user.id
			redirect_to '/messages'
		end
	end

	def wall
		@who = User.find(session[:id])
		@messages = Message.all
		@comments = Comment.all
		render 'wall'
	end

	def logout
		session[:id] = nil
		@who = nil
		redirect_to '/users/new'
	end

	def process_message
		Message.create(content: params[:content], user_id: session[:id])
		redirect_to '/messages'
	end

	def process_comment
		Comment.create(content: params[:content], user_id: session[:id], message_id: params[:message_id])
		redirect_to '/messages'
	end

end
