class AuthController < ApplicationController
  def signup
    @user = User.new(
      username: params[:username],
      email: params[:email],
      password: params[:password],
    )

    if @user.save
      render json: { msg: "Created User", data: UserSerializer.new(@user) }, status: :created
    else
      render json: { err: @user.errors.full_messages },
             status: :unprocessable_entity
    end
  end

  def verify
    header = request.headers["Authorization"]
    token = header.split(" ").last if header
    @decoded = decode_jwt(token)
    render json: @decoded
  end

  def login
    @user = User.find_by(username: params[:username])

    if @user&.authenticate(params[:password])
      token, exp = encode_jwt({ uid: @user.id.to_s })

      render status: :ok, json: {
               msg: "Logged in Successfully",
               data: {
                 token: token,
                 exp: exp,
                 user: UserSerializer.new(@user),
               },
             }
    else
      render status: :unauthorized, json: { err: "Username and password don't match" }
    end
  end
end
