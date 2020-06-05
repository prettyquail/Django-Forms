from django.db import models

# Create your models here.
class Register(models.Model):
	username=models.CharField(max_length=55)
	email=models.EmailField(max_length=66)
	password=models.CharField(max_length=66)