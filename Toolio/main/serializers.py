from rest_framework import serializers
from django.db import models

from .models import ad

class adSerializer(serializers.ModelSerializer):
  user = models.ForeignKey(source="user_id")
  
  isRequest = serializers.BooleanField(source="isRequest")
  title = serializers.CharField(source="title")
  date = serializers.DateField(source="date")
  price = serializers.IntegerField(source="price")
  description = serializers.CharField(source="description")
  image = serializers.ImageField(source="image")
  isRented = serializers.BooleanField(source="isRented")
  
  class Meta:
    model = ad
    fields=['isRequest', 'title', 'date', 'price', 'description', 'image', 'user', 'isRented']