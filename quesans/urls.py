"""quesans URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from api import views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static


router=DefaultRouter()
# router.register("user/signup",views.SignupView,basename="sign")
# router.register("ques",views.QuesView,basename="ques")

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('index/',views.TemplateView.as_view(),name="index"),
    path('register/',views.Signupview.as_view(),name="sign"),
    path("",views.LoginView.as_view(),name="log"),
    path("details/<int:id>",views.QuestinDetailView.as_view(),name="detail"),
    path("questin/<int:id>/add_answer",views.add_Answer,name="addans"),
    path("answer/<int:id>/add_vote",views.upvote,name="upvote"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
