class User < ApplicationRecord
  has_secure_password
  validates :username, presence: true, uniqueness: true
  validates :email, presence: true, format: { with: URI::MailTo::EMAIL_REGEXP }

  PASSWORD_REQUIREMENTS = / \A
        (?=.*\d) #Contain atleast one number
    /x

  validates :password,
            length: { minimum: 6 },
            format: { with: PASSWORD_REQUIREMENTS, message: "should contain atleast one number" }
end
