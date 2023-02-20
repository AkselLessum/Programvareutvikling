from rest_framework import serializers

from .models import ad

class adSerializer(serializers.ModelSerializer):
  isRequest = serializers.BooleanField(source="isRequest")
  title = serializers.CharField(source="title")
  date = serializers.DateField(source="date")
  price = serializers.IntegerField(source="price")
  description = serializers.CharField(source="description")
  image = serializers.ImageField(source="image")
  
  class Meta:
    model = ad
    fields=['isRequest', 'title', 'date', 'price', 'description', 'image']