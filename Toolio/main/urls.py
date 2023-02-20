from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('createAd/', views.createAd, name="createAd"),
    path('userPage/', views.userPage, name="userPage"),
    path("edit_ad/<int:ad_id>/", views.edit_ad, name="edit_ad"),
    path('delete/<int:ad_id>/', views.delete_ad, name='delete_ad'),


]