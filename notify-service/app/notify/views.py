from .models import DepositNotification, ReferralRewardNotification
from rest_framework.decorators import api_view
from rest_framework.response import Response
from notify.permissions import IsAuthenticated
from rest_framework.views import APIView
from notify.utils import get_uid_from_request

class GetUserNotifications(APIView):
    """
    Get the user notifications

    :param request: The request object
    :return: The user notifications

    :raises AuthenticationFailed: If the token is invalid
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        uid = get_uid_from_request(request)

        all_notifications = []
        try:
            deposit_query = DepositNotification.objects.filter(uid=uid)
            referral_reward_query = ReferralRewardNotification.objects.filter(uid=uid)
        except Exception as e:
            return Response({"error": str(e)})

        for notification in deposit_query.values():
            notification['type'] = 'D'
            all_notifications.append(notification)

        for notification in referral_reward_query.values():
            notification['type'] = 'R'
            all_notifications.append(notification)

        # Sort the notifications by created_at
        all_notifications.sort(key=lambda x: x['created_at'], reverse=True)

        # Return the notifications
        return Response({"notifications": all_notifications})