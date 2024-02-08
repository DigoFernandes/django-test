from pyexpat import model
from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_user = models.AutoField(primary_key=True)
    username = models.TextField(max_length=255)
    password = models.IntegerField()