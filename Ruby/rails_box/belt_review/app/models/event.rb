class Event < ActiveRecord::Base
  belongs_to :user
  has_many :comments
  has_many :users, through: :calendars
  has_many :calendars

  DATE_REGEX = /\A(?:0?[1-9]|1[0-2])\/(?:0?[1-9]|[1-2]\d|3[01])\/\d{4}\Z/
  validates :name, presence: true, length: { minimum: 4 }
  validates :date, presence: true, format: { with: DATE_REGEX }
  validates :location, :state, presence: true
end
