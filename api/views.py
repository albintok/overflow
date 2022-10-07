from django.shortcuts import render
from api.models import Questions,Answers
from serializers import QuesSerializer,UserSerializer
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework.decorators import action


# Create your views here.

class SignupView(ViewSet):
    def create(self,request,*args,**kwargs,):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

# localhost:8000/ques/
class QuesView(ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def list(self, request, *args, **kwargs):
       all_ques=Questions.objects.all()
       serializer=QuesSerializer(all_ques,many=True)
       return Response(data=serializer.data)

