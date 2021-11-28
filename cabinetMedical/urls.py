from django.urls import path
from . import views

urlpatterns = [
    path('client/<str:pk>', views.client , name="client"), 
    path('about/', views.about), 
    path('', views.home , name="home"), 
    path('book/', views.boook , name="book"), 
    path('create', views.create , name="create"), 
    path('update/<str:pk>', views.update , name="update"),
    path('delete/<str:pk>', views.delete , name="delete"),
] 