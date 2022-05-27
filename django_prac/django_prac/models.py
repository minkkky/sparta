#user/models.py
from django.db import models


# Create your models here.
class UserModel(models.Model):
    email = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=256, null=False)

    def __init__(self):
        print('새로 가입했어요')