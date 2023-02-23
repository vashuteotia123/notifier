from rest_framework.serializers import ModelSerializer
from .models import DepositNotification, ReferralRewardNotification

class DepositNotificationSerializer(ModelSerializer):
    class Meta:
        model = DepositNotification
        fields = '__all__'
        

class ReferralRewardNotificationSerializer(ModelSerializer):
    class Meta:
        model = ReferralRewardNotification
        fields = '__all__'
        