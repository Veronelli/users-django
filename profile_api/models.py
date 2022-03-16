from statistics import mode
from django.db import models

"""Modelo db para articulos"""
class Area(models.Model):
    _id = models.AutoField(primary_key=True)
    _area = models.CharField(max_length=24,null=False, unique=True)
    
    """ Id funcion"""
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
        
    """ Area """
    @property
    def area(self):
        return self._area
    
    @area.setter
    def area(self,a):
        self._area = a

""""Modelo para db de Usuario"""
class UserProfile(models.Model):
    _id = models.AutoField(primary_key=True)
    _name = models.CharField(max_length=255, unique=True)
    _password = models.CharField(max_length=255)
    _area = models.ForeignKey('Area', on_delete=models.CASCADE)

    @property
    def id(self):
        return self.id
        
    @id.setter
    def id(self,i):
        self._id = i

    """ Email funcion """    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, p):
        self._password = p
    
    """ Name funcion """    
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, name):
        self._name = name
        
        
    def __str__(self):
        return f"Name: {self._name}, Email: {self._password}, Area: {self._area.area}"
    
