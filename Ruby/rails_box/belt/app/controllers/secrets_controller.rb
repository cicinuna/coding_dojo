class SecretsController < ApplicationController
    def create
        secret = Secret.new(content: params[:content], user_id: current_user.id)
        if secret.save
            flash[:errors] = ["Successfully Posted a Secret!"]
            redirect_to '/secrets'
        else
            flash[:errors] = secret.errors.full_messages
            redirect_to "/users/#{session[:user_id]}"
        end
    end

    def show
        if session[:user_id] == nil
            flash[:errors] = ["You Must be Logged in to view this page!"]
            redirect_to '/sessions/new'
        else    
            @secrets = Secret.all
            @count = 0
            current = User.find(current_user.id)
            @user_secrets = current.secrets
            @users = User.all
            @user_secrets.each do |s|
                @users.each do |u|
                    u.likes.each do |p|
                        if p.secret_id == s.id
                            @count += 1
                        end
                    end
                end
            end     
            render 'secrets'
        end
    end 

    def like
        like = Like.new(user_id: current_user.id, secret_id: params[:secret_id])

        if like.save
            flash[:errors] = ["Successfully Liked this secret!"]
            redirect_to '/secrets'
        else
            flash[:errors] = like.errors.full_messages
            redirect_to :back
        end
    end

end
