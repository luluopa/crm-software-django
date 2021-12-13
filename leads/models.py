from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
import datetime

class User(AbstractUser):
    is_organisor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class Lead(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    phone_number = models.CharField(blank=True, null=True, max_length=15)
    data_created = models.DateField(auto_now_add=True)

    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    agent = models.ForeignKey('Agent', blank=True, null=True, on_delete=models.SET_NULL) #Cascade means when agent is deleted leads is deleted too
    category = models.ForeignKey('Category', related_name='leads', blank=True, null=True, on_delete=models.SET_NULL)

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=128)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

def post_created_user_profile(instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_created_user_profile, sender=User)