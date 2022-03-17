from django.db import models

"""Modelo db para articulos"""
class Area(models.Model):
    id = models.AutoField(primary_key=True, name='id')
    area = models.CharField(max_length=24,null=False, unique=True)
    
    def __str__(self):
        return f"Id: {self.id}, Area: {self.area}"

""""Modelo para db de Usuario"""
class UserProfile(models.Model):
    id = models.AutoField(primary_key=True,name='id')
    name = models.CharField(max_length=255, name='name', unique=True)
    password = models.CharField(max_length=255, name='password')
    area = models.ForeignKey(Area,related_name="_id", on_delete=models.CASCADE)
        
    def __str__(self):
        return f"Name: {self.name}, Password: {self.password}, Area: {self.area.area}"
    
