class ApplicationController < ActionController::Base
  # Prevent CSRF attacks by raising an exception.
  # For APIs, you may want to use :null_session instead.
  protect_from_forgery with: :exception

  def hello
    render text: "Hello Coding Dojo!"
  end

  def times
    if session[:times].nil?
      session[:times] = 0
    end
    session[:times] += 1

    render text: "You've visited this page #{session[:times]} times!"
  end
  
  def restart
    session[:times] = nil
    render text: "Destroyed the session!"
  end

end
