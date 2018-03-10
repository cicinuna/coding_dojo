class User < ActiveRecord::Base
  has_secure_password
  has_many :events
  has_many :calendars
  has_many :events_attending, through: :calendars, source: :event
  has_many :comments

  EMAIL_REGEX = /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]+)\z/i
  validates :first_name, :last_name, presence: true, length: { minimum: 2 }
  validates :email, presence: true, uniqueness: { case_sensitive: false }, format: { with: EMAIL_REGEX }
  validates :password, length: { minimum: 8 }
  validates :location, presence: true

  before_save :downcase_email

  private
    def downcase_email
      self.email.downcase!
    end
end
