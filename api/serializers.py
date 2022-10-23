from rest_framework import serializers
from api.models import Questions,Answers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=User
        fields=["id","username","password"]
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
class Usernameserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username"]
class AnsSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    ques=serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)
    up_voted=Usernameserializer(many=True,read_only=True)
    def create(self, validated_data):
        user=self.context.get("user")
        return Answers.objects.create(**validated_data,user=user)




