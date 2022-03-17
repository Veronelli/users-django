from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.conf.urls import url
from rest_framework import viewsets

from rest_framework_swagger.views import get_swagger_view
from .serealizers import UserProfileSerializer, AreaSerializer
from .models import UserProfile, Area

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^$', schema_view)
]

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all().order_by('name')
    serializer_class = UserProfileSerializer
    
    def hola(request):
        return JsonResponse({"Hello":"Hello"})
    
class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all().order_by('area')
    serializer_class = AreaSerializer
    