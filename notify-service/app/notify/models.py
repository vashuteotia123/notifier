from django.db import models
from rest_framework import serializers

class DepositNotification(models.Model):
        uid = models.CharField(null=False, blank=False, max_length=255)
        token_id = models.CharField(null=False, blank=False, max_length=255)
        blockchain_deposit_status = models.CharField(null=False, blank=False, max_length=255)
        brine_deposit_status = models.CharField(default=None, max_length=255)
        deposit_blockchain_hash = models.CharField(null=False, blank=False, max_length=255)
        amount = models.CharField(null=False, blank=False, max_length=255)
        created_at = models.DateTimeField(auto_now_add=True)

class ReferralRewardNotification(models.Model):

    STATUS_LIST = (
        ('PENDING', 'PENDING'),
        ('COMPLETED', 'COMPLETED'),
        ('FAILED', 'FAILED'),
    )

    uid = models.CharField(null=False, blank=False, max_length=255)
    id = models.IntegerField(primary_key=True)
    status = models.CharField(choices=STATUS_LIST, max_length=255)
    currency = models.CharField(null=False, blank=False, max_length=255)
    trading_fee_reward = models.DecimalField(max_digits=32, decimal_places=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



