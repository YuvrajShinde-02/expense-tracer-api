from typing_extensions import Required
from rest_framework import serializers
from restapi import models


class Expense(serializers.ModelSerializer):
    amount = serializers.FloatField(required=True)
    merchant = serializers.CharField(required=True)
    decription = serializers.CharField(required=False)
    category = serializers.CharField(required=True)
    date_created = serializers.DateTimeField(required=False)
    date_update = serializers.DateTimeField(required=False)

    class Meta:
        model = models.Expense
        fields = "__all__"
        read_only_fields = ["id", "date_created", "date_update"]
