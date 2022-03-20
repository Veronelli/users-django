import jwt, environ, datetime, os
from .models import UserProfile
env = environ.Env()
from django.http import JsonResponse

BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
environ.Env.read_env(os.path.join(BASE_DIR,'.env'))

class ProfileApiMiddleware:
    def __init__(self,get_response):
        self.secret_key = env('SECRET_KEY')
        self.get_response = get_response  
        
    def __call__(self,request):
        request.saludo = "Hola"
        response = self.get_response(request)

        if '/api/user' in request.path:
            try:
                token = request.headers['Token']
                id_token = jwt.decode(token,self.secret_key,algorithms=['HS256'])['id']
                if UserProfile.objects.filter(id=id_token).exists:
                    return response

            except KeyError as ex:
                return JsonResponse({"message":"Se Necesita un token valido"})
            except jwt.exceptions.DecodeError:
                return JsonResponse({"message":"El token no es valido"})
    
    