from django.contrib import admin
from .models import UserProfile,Area

# Register your models here.
admin.site.register([UserProfile,Area])
