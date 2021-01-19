from rest_framework import serializers
from .models import Customer


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'fullname', 'mobile', 'email']