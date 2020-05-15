from django.db import models

# Create your models here.
class Usersreg(models.Model):
    User_name=models.CharField('User_name',max_length=10)
    user_email=models.EmailField(max_length=30)
    passw=models.CharField('password',max_length=10)