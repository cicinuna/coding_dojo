class User < ActiveRecord::Base
    has_many :messages
    has_many :comments
    validates :username, presence: true, uniqueness: { case_sensitive: false }, length: { minimum: 5 }
end
