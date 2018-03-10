class SessionsController < ApplicationController
    def new
        render 'new'
    end

    def create
        user = User.find_by(email: params[:email])
        if !user
            flash[:errors] = ["Please Register!"]
            redirect_to :back
        else
            if user && user.authenticate(params[:password])
                session[:user_id] = user.id
                redirect_to "/users/#{user.id}"
            else
                flash[:errors] = ["Invalid Login Information!"]
                redirect_to :back
            end
        end
    end

    def destroy
        session[:user_id] = nil;
        flash[:errors] = ["Successfully Logged Out!"]
        redirect_to '/sessions/new'
    end
end
