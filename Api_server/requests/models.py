from django.db import models

# Create your models here.
class ProjectCreateQ(models.Model):
    sid=models.CharField('SID',max_length=10)
    user_name=models.CharField('USER_NAME',max_length=15)
    dimage=models.CharField('IMAGE',max_length=10)
    status=models.BooleanField()


