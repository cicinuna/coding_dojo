class RpgsController < ApplicationController

    def index
        if session[:gold].nil?
            session[:gold] = 0
        end
        if session[:activities].nil?
            session[:activities] = []
        end
        render "index"
    end

    def farm
        earning = rand(10...20)
        session[:gold] += earning
        session[:activities].push("You've entered farm and gained #{earning} golds!")
        redirect_to '/'
    end

    def cave
        earning = rand(5...10)
        session[:gold] += earning
        session[:activities].push("You've entered cave and gained #{earning} golds!")
        redirect_to '/'
    end

    def house
        earning = rand(2...5)
        session[:gold] += earning
        session[:activities].push("You've entered house and gained #{earning} golds!")
        redirect_to '/'
    end

    def casino
        earning = rand(-50...50)
        session[:gold] += earning
        if earning < 0
            session[:activities].push("You've entered casino and lost #{earning} golds... ouch!")
        else
            session[:activities].push("You've entered casino and gained #{earning} golds!")
        end
        redirect_to '/'
    end
end
