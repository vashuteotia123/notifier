Rails.application.routes.draw do
  get "/signup", to: "auth#signup"
  get "/login", to: "auth#login"
  get "/", to: "notifications#notifications"
end
