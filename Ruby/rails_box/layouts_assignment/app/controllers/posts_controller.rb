class PostsController < ApplicationController

    def index
        @posts = Post.all
        @users = User.all
        render "three_column"
    end

    def add
        Post.create( user_params )
        redirect_to '/posts'
    end

    private
        def user_params
            params.require(:post).permit(:title, :content, :user_id)
        end
end
