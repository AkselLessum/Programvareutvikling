from django.urls import path
from . import views
from user import views as v

urlpatterns = [
    path('', views.home, name="home"),
    path('createAd/', views.createAd, name="createAd"),
    path('register/', v.register, name="register"),
]
