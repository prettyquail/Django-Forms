from django.urls import path
from . import views
from ModelForm.views import registeruser,loginuser,logoutuser,indexpage

urlpatterns = [
    path('registeruser/', views.registeruser,name='registeruser'),
    path('loginuser/', views.loginuser,name='loginuser'),
    path('logoutuser/', views.logoutuser, name="logoutuser"),
    path('indexpage/', views.indexpage,name='indexpage'),
   
]