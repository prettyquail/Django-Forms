from django.urls import path
from . import views
from .views import register

urlpatterns = [
    path('register/', views.register,name='register'),
    path('login/', views.loginPage,name='login'),
    path('logout/', views.logoutUser, name="logout"),
    path('index/', views.index,name='index'),
   
]