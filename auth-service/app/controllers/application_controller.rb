class ApplicationController < ActionController::API
  def encode_jwt(payload, exp = 24.hours.from_now)
    private_key = OpenSSL::PKey::RSA.new File.read "private_key.pem"
    payload[:exp] = exp.to_i
    return JWT.encode(payload, private_key, "RS256"), exp
  end

  def decode_jwt(token)
    public_key = OpenSSL::PKey::RSA.new File.read "private_key.pem"
    decoded = JWT.decode(token, public_key, true, algorithm: "RS256")[0]
    HashWithIndifferentAccess.new decoded
  end
end
