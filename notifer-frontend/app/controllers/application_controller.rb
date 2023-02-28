class ApplicationController < ActionController::Base
  def decode_jwt(token)
    public_key = OpenSSL::PKey::RSA.new File.read "public_key.pem"
    decoded = JWT.decode(token, public_key, true, algorithm: "RS256")[0]
    HashWithIndifferentAccess.new decoded
  end
end
