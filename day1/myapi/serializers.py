from dataclasses import fields
from rest_framework import serializers
from affairs.models import student

class studserislizer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields=['name' , 'address' , 'bdate' , 'mail' ]

    