from django.shortcuts import render
from api.models import Questions,Answers
from api.serializers import QuesSerializer,UserSerializer
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework.decorators import action
from django.views.generic import View,TemplateView

# Create your views here.
class TemplateView(TemplateView):
    template_name="index.html"

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
    serializer_class = QuesSerializer
    queryset = Questions.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def create(self, request, *args, **kwargs):
        serilaizer=QuesSerializer(data=request.data,context={"user":request.user})
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data)
        else:
            return Response(serilaizer.errors)
    @action(methods=["GET"],detail=False)
    def my_ques(self,request, *args, **kwargs):
        user=request.user
        qs=user.questions_set.all()
        serilaizer=QuesSerializer(qs,many=True)
        return Response(data=serilaizer.data)
    @action(methods=["GET"],detail=True)
    def Ques_detail(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        que=Questions.objects.get(id=id)
        serilaizer=QuesSerializer(que,many=False)
        return Response(data=serilaizer.data)







