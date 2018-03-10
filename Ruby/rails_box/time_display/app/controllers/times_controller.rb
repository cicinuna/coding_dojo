class TimesController < ApplicationController

    def main
        @date = DateTime.now.to_date
        @time = DateTime.now.strftime("%I:%M%p")
        render "time"
    end

end
