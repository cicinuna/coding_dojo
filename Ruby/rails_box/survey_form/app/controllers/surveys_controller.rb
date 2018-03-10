class SurveysController < ApplicationController

    def index
        render "survey"
    end

    def submit
        @input = {name: params[:name], location: params[:location], language: params[:language], comment: params[:comment]}
        if session[:times].nil?
            session[:times] = 1
        else
            session[:times] += 1
        end
        flash[:success] = "Thanks for submitting this form! You have submitted this form #{session[:times]} times now!"
        render "results"
    end

end
