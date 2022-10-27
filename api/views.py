from django.shortcuts import render,redirect
from api.models import MyUser, Questions,Answers

from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework.decorators import action
from django.views.generic import View,TemplateView
from api.forms import RegistrationForm,LoginForm,QuestinForm
from django.views.generic import CreateView,FormView,ListView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.decorators import method_decorator
# Create your views here.


class TemplateView(CreateView,ListView):
    template_name="home.html"
    form_class=QuestinForm
    model=Questions
    success_url=reverse_lazy("index")
    context_object_name="questins"

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    def get_queryset(self):
        return Questions.objects.all().exclude(user=self.request.user)

class Signupview(CreateView):
    model=MyUser
    form_class=RegistrationForm
    template_name="register.html"
    success_url=reverse_lazy("sign")

def required_signin(fn):
    def inner(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"u must login")
            return redirect("log")
        else:
            return fn(request,*args,**kwargs)
    return inner

class LoginView(FormView):
    form_class=LoginForm
    template_name="login.html"
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"Login sucess")
                return redirect("index")
            else:
                messages.error(request,"login failed")
                return redirect("index")

class QuestinDetailView(DetailView):
    model= Questions
    template_name="questin-detail.html"
    pk_url_kwarg: str="id"
    context_object_name: str="questin"


#localhost:8000/questin/{id}/answer
def add_Answer(request,*args,**kwargs):
    qid=kwargs.get("id")
    quest=Questions.objects.get(id=qid)
    ans=request.POST.get("answer")
    Answers.objects.create(user=request.user,answer=ans,ques=quest)
    return redirect("index")




@required_signin
def sign_out(request,*args,**kwargs):
    logout(request)
    return redirect("log")





# class SignupView(ViewSet):
#     def create(self,request,*args,**kwargs,):
#         serializer=UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)

# # localhost:8000/ques/
# class QuesView(ModelViewSet):
#     serializer_class = QuesSerializer
#     queryset = Questions.objects.all()
#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
#     def create(self, request, *args, **kwargs):
#         serilaizer=QuesSerializer(data=request.data,context={"user":request.user})
#         if serilaizer.is_valid():
#             serilaizer.save()
#             return Response(serilaizer.data)
#         else:
#             return Response(serilaizer.errors)
#     @action(methods=["GET"],detail=False)
#     def my_ques(self,request, *args, **kwargs):
#         user=request.user
#         qs=user.questions_set.all()
#         serilaizer=QuesSerializer(qs,many=True)
#         return Response(data=serilaizer.data)
#     @action(methods=["GET"],detail=True)
#     def Ques_detail(self,request,*args,**kwargs):
#         id=kwargs.get("pk")
#         que=Questions.objects.get(id=id)
#         serilaizer=QuesSerializer(que,many=False)
#         return Response(data=serilaizer.data)







