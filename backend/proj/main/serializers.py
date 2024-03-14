from rest_framework import serializers
from .models import Customer, Helper, Skill

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'rating']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name']  # Fields to include in the serialization

class HelperSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(many=True, read_only=True)  # Nested serialization for related Skill objects

    class Meta:
        model = Helper
        fields = ['id', 'name', 'skill']  # Fields to include in the serialization
