class SessionsController < ApplicationController
  def new
    render 'login'
  end

  def create
    if params[:password].eql? params[:password_confirmation]
      User.create(email: params[:email], name: params[:name], password: params[:password], password_confirmation: params[:password_confirmation])
      session[:user_id] = User.last.id
      redirect_to "/users/#{User.last.id}"
    else
      flash[:errors] = ["Passwords must match in order to register!"]
      redirect_to :back
    end
  end

  def destroy
  end

  def login
    render 'login'
  end

end
