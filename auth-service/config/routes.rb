Rails.application.routes.draw do
  post "auth/signup"
  post "auth/login"
  get "auth/verify"
end
