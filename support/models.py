from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
# Create your models here.
class User(AbstractUser):
    phone=models.CharField(max_length=12,unique=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username
    
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
post_save.connect(create_profile,User)