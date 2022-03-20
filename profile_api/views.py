
from django.http import JsonResponse
from django.conf.urls import url

from rest_framework import viewsets
from rest_framework_swagger.views import get_swagger_view
from .serealizers import UserProfileSerializer, AreaSerializer

from .models import UserProfile, Area
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view
from django.utils.decorators import decorator_from_middleware

from .serealizers import UserProfileSerializer
import jwt,datetime, environ, os

schema_view = get_swagger_view(title='Pastebin API')

env = environ.Env()
BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

environ.Env.read_env(os.path.join(BASE_DIR,'.env'))

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
    
class Login():
        
    @api_view(['POST'])
    def post(request):
        name = request.data['name']
        password = request.data['password']        
        secret_key = env('SECRET_KEY')
        user = UserProfile.objects.filter(name=name).first()
        print(request.saludo)
        if user is None:
            raise AuthenticationFailed('User not found!')
        
        valid = UserProfileSerializer.validPassword(password1 = user.password, password2 = password)
        
        if not valid:
            raise AuthenticationFailed('Incorrect password')
        
        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow()
        }
        
        token = jwt.encode(payload,secret_key,algorithm='HS256')
        print(token)
        response = JsonResponse({
            'jwt':token
        })
        
        return response