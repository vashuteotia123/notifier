class AuthController < ApplicationController
  def signup
    @user = User.new(
      username: params[:username],
      email: params[:email],
      password: params[:password],
    )

    if @user.save
      logger.info("Created user with user_id: #{@user.id}")
      render json: { msg: "Created User", data: UserSerializer.new(@user) }, status: :created
    else
      logger.warn("Failed to create new user with errors: #{@user.errors.full_messages.to_s}")
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
      logger.info("Generated JWT token for user_id: #{@user.id}")
      render status: :ok, json: {
               msg: "Logged in Successfully",
               data: {
                 token: token,
                 exp: exp,
                 user: UserSerializer.new(@user),
               },
             }
    else
      logger.warn("Password authentication failed")
      render status: :unauthorized, json: { err: "Username and password don't match" }
    end
  end
end
