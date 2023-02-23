from rest_framework.permissions import BasePermission
from notify.utils import get_uid_from_request

class IsAuthenticated(BasePermission):

    """
    Check if the user is authenticated
    """
    def has_permission(self, request, view):
        if get_uid_from_request(request) is None:
            return False
        return True