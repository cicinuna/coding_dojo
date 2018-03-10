class UsersController < ApplicationController

    def index
        @users = User.all
        render "two_column"
    end 

    def add
        User.create( user_params )
        redirect_to "/users"
    end

    private 
        def user_params
            params.require(:user).permit(:first_name, :last_name, :favorite_language)
        end
end
