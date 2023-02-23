from django.contrib import admin
from .models import DepositNotification, ReferralRewardNotification

class DepositNotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'token_id', 'blockchain_deposit_status', 'brine_deposit_status', 'deposit_blockchain_hash', 'amount', 'created_at')


admin.site.register(DepositNotification, DepositNotificationAdmin)
admin.site.register(ReferralRewardNotification)
