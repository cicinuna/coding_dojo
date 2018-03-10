class UsersController < ApplicationController
    def new
        render 'new'
    end

    def create
        user = User.new(user_params)
        if user.save
            flash[:errors] = ["Successfully Registered! Please Log In to access Dojo Secret Wall"]
            redirect_to '/sessions/new'
        else
            flash[:errors] = user.errors.full_messages
            redirect_to :back
        end
    end

    def show
        if session[:user_id] == nil
            flash[:errors] = ["You are not logged in!"]
            redirect_to '/sessions/new'
        else
            page = User.find(params[:id])
            puts current_user == page
            if current_user != page
                flash[:errors] = ["You do not have the permission to view another user's page"]
                redirect_to "/users/#{current_user.id}"
            else
                @user = User.find(session[:user_id])
                render 'show'
            end
        end
    end

    def edit
        if session[:user_id] == nil
            flash[:errors] = ["You are not logged in!"]
            redirect_to '/sessions/new'
        else
            page = User.find(params[:id])
            if current_user != page
                flash[:errors] = ["You do not have the permission to edit another user's page"]
                redirect_to "/users/#{current_user.id}"
            else
                @user = User.find(session[:user_id])
                render 'edit'
            end
        end
    end

    def update
        user = User.find(params[:id])
        did_update = user.update(name: params[:name], email: params[:email])
        if did_update
            flash[:errors] = ["Successfully Modified User Information!"]
            redirect_to "/users/#{params[:id]}"
        else
            flash[:errors] = user.errors.full_messages
            redirect_to :back
        end
    end

    private
      def user_params
        params.require(:user).permit(:email, :name, :password, :password_confirmation)
      end
end
