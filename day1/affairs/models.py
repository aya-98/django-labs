from django.db import models

class studnent(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    mail=models.EmailField()
    bdate=models.DateField()
    address=models.CharField(max_length=40)

class track(models.Model):
    name = models.CharField(max_length=20)


class intake(models.Model):
    name = models.CharField(max_length=20)


# Create your models here.
