from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(
        default='profile.png', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
