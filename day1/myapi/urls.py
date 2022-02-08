from django.urls import path , include
from rest_framework import routers
from .views import liststud
from .views import rest_api
router=routers.DefaultRouter()
router.register(r'student' , liststud )

urlpatterns = [
    path('' , include(router.urls)) ,
    path('api-auth/', include('rest_framework.urls' , namespace='rest_framework')) ,
    path('rest-api/<id>' , rest_api)

]
