from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.client), 
    path('about/', views.about), 
    path('user/', views.user), 
    path('page/', views.page), 
    path('', views.home), 
    path('book/', views.boook), 
    path('projet3', views.projet3), 
]