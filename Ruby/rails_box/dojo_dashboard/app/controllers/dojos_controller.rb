class DojosController < ApplicationController

    def index
        @dojos = Dojo.all
        render 'index'
    end

    def new
        render 'new'
    end

    def create
        Dojo.create( user_params )
        redirect_to '/dojos'
    end 

    def show
        @dojo = Dojo.find(params[:id])
        render 'show'
    end

    def edit
        @dojo = Dojo.find(params[:id])
        render 'edit'
    end

    def update
        @dojo = Dojo.find(params[:id])
        @dojo.update(user_params)
        redirect_to '/dojos'
    end

    def destroy
        @dojo = Dojo.find(params[:id])
        @dojo.destroy
        redirect_to '/dojos'
    end
    private
        def user_params
            params.require(:dojo).permit(:branch, :street, :city, :state)
        end
end
