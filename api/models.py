from distutils.command.upload import upload
from email.policy import default
from itertools import count
from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.db.models import Count


class MyUser(AbstractUser):
    pro_pic=models.ImageField(upload_to="profile_pics",null=True)
    phone=models.PositiveIntegerField()
    email=models.CharField(max_length=100)

class Questions(models.Model):
    questin=models.CharField(max_length=300)
    image=models.ImageField(null=True,upload_to="qimages",blank=True)
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)

    @property
    def fetch_answers(self):
        answers=self.answers_set.all().annotate(count=Count('up_voted')).order_by(-count)
        return answers

    def __str__(self):
        return self.questin

class Answers(models.Model):
    answer=models.CharField(max_length=300)
    ques=models.ForeignKey(Questions,on_delete=models.CASCADE)
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    up_voted=models.ManyToManyField(MyUser,related_name="vote")

# Create your models here.
