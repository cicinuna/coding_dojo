class UsersController < ApplicationController
	def index
		render 'login'
	end

	def register
		user = User.new(user_params)
		if user.save
			flash[:successes] = ["Successfully Registered! Please Log In!"]
			redirect_to '/'
		else
			flash[:errors] = user.errors.full_messages
			redirect_to :back
		end
	end

	def login
		user = User.find_by(email: params[:email])
		if !user
			flash[:errors] = ["Please Register!"]
			redirect_to :back
		else
			if user && user.authenticate(params[:password])
				session[:user_id] = user.id
				redirect_to "/events"
			else
				flash[:errors] = ["Invalid Login Information!"]
				redirect_to :back
			end
		end
	end

	def destroy
		session[:user_id] = nil;
		flash[:successes] = ["Successfully Logged Out!"]
		redirect_to '/'
	end

	def show
		render 'show'
	end

	private
		def user_params
			params.require(:user).permit(:first_name, :last_name, :email, :location, :state, :password, :password_confirmation)
		end
end
