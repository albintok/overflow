from rest_framework import serializers
from models import Questions,Answers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=User
        fields=["username","password"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class QuesSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Questions
        exclude=("created_date",)
    def create(self, validated_data):
        user=self.context.get("user")
        return Questions.objects.create(**validated_data,user=user)




