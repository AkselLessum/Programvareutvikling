from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, Group, Permission


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='profile.png', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
    
class CustomUser(AbstractUser):
    phone_number = models.IntegerField(unique=True)
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, help_text='The groups this user belongs to.', related_name='user_customuser')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, help_text='Specific permissions for this user.', related_name='user_customuser')
