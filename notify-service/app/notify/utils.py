import jwt, os
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed

def get_uid_from_request(request):

    """
    Get the uid from the request

    :param request: The request object
    :return: The uid

    :raises AuthenticationFailed: If the token is invalid
    """

    authorization_header = request.META.get('HTTP_AUTHORIZATION')
    if not authorization_header:
        return None

    try:
        token = authorization_header.split()[1]
        pub_key = os.environ.get('AUTH_PUBLIC_KEY')
        payload = jwt.decode(token, pub_key, algorithms=['RS256'])
        return payload['uid']
    except (jwt.exceptions.DecodeError, KeyError):
        raise AuthenticationFailed('Invalid token')
    

def validate_notification(notification):
    required_keys = ["type", "uid", "token_id", "blockchain_deposit_status", 
                     "brine_deposit_status", "deposit_blockchain_hash", 
                     "amount", "created_at"]
    
    if not all(key in notification for key in required_keys):
        return False, "Missing required keys"
    
    if not all(notification[key] for key in notification):
        return False, "Missing required values"
    
    try:
        float(notification["amount"])
    except ValueError:
        return False, "Invalid amount"
    
    return True
