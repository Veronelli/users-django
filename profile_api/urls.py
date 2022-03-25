from unicodedata import name
from django.urls import include,path
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from . import views

router = routers.SimpleRouter()
router.register(r'user',views.UserViewSet)
router.register('area',views.AreaViewSet)

schema_view = get_swagger_view(title='Users project Swagger')

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    path(r'swagger/', schema_view),
    path('status/',views.server_status, name="Hola"),
    path('login',views.Login.post)
]
