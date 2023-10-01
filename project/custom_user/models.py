from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import CustomUserManager
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save

    
class customuser(AbstractBaseUser, PermissionsMixin):
    objects = CustomUserManager()
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email = models.EmailField(unique=True) 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.email
    


class Profile(models.Model):
    user=models.OneToOneField(customuser,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.email} Profile"

@receiver(post_save, sender=customuser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


    




