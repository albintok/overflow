from django.db import models
from django.contrib.auth.models import User

class Questions(models.Model):
    questin=models.CharField(max_length=300)
    image=models.ImageField(null=True,upload_to="qimages")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)

class Answers(models.Model):
    answer=models.CharField(max_length=300)
    ques=models.ForeignKey(Questions,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="ansuser")
    date=models.DateTimeField(auto_now_add=True)
    up_voted=models.ManyToManyField(User)

# Create your models here.
