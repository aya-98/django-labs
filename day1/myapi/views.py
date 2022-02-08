from django.shortcuts import render
from rest_framework import viewsets
from affairs.models import student
from .serializers import studserislizer
from rest_framework.decorators import api_view
from rest_framework import status 
from rest_framework.response import Response

class liststud(viewsets.ModelViewSet):
    queryset=student.objects.all()
    serializer_class=studserislizer

@api_view(['GET'  ,'PUT' ,'DELETE'])
def rest_api(req ,id):
    try:

        stud=student.objects.get(id=id)

    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    if req.method=='GET':
        stud_serial=studserislizer(stud)
        return Response(stud_serial.data)
    
    elif req.method=='PUT':
        stud_serial=studserislizer(stud ,data=req.data)
        if stud_serial.is_valid():
            stud_serial.save()
            return Response(stud_serial.data)
        
        return Response(stud_serial.errors , status=status.HTTP_400_BAD_REQUEST)

    elif req.method=='DELETE':
        stud.delete()
        return Response({'msg': 'student deleted successfully'} , status=status.HTTP_204_NO_CONTENT)


