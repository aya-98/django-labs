from django.db import models

class myuser(models.Model):
    name=models.CharField(max_length=30)
    mail=models.EmailField()
    passwd =models.CharField(max_length=30)


# Create your models here.
