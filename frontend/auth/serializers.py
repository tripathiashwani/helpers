from rest_framework import serializers
from .models import Customer, Helper

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'age']  # Fields to include in the serialization

class HelperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Helper
        fields = ['id', 'name', 'skill']  # Fields to include in the serialization
