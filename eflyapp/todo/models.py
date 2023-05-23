from django.db import models
from .choices import *
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


#Modelo de city-lights
class Address(models.Model):
   country = models.ForeignKey('cities_light.Country', on_delete=models.SET_NULL, null=True, blank=True) 
   city = models.ForeignKey('cities_light.City', on_delete=models.SET_NULL, null=True, blank=True)
   
#Pruebas

class CustomUser(AbstractUser):
    DNI=models.IntegerField(primary_key=True, default=0)
    saldo=models.IntegerField(default=0)
    fechaNaci=models.DateField(null=True)
    lugarNaci= models.ForeignKey('cities_light.City', on_delete=models.SET_NULL, null=True, blank=True)
    dirFact=models.CharField(max_length=100,null=True)
    sexo=models.CharField(max_length=20,choices=genero,default='N')
    tipoUsuario=models.CharField(max_length=20,null=True)
    email = models.EmailField(unique=True)
    picture=models.ImageField(default='profile_default.png',upload_to='users/')

    
#Tablas BD
class Ciudad(models.Model):
    nombreCiudad=models.CharField(max_length=100)
    pais=models.CharField(max_length=100)
    hora=models.TimeField()

    def __str__(self):
        return self.nombreCiudad

class Vuelo(models.Model):
    codigo = models.CharField(unique=True, null=True, max_length=10)
    origen = models.ForeignKey('cities_light.City', on_delete=models.CASCADE, related_name="origenes", limit_choices_to={'name__in': ['Pereira', 'Bogotá', 'Medellín']})
    destino= models.ForeignKey('cities_light.City', on_delete=models.CASCADE, related_name="destinos", limit_choices_to={'name__in': ['Pereira', 'Bogotá', 'Medellín']})
    horaSalida=models.DateTimeField()
    horaLlegada=models.DateTimeField()
    precioPrimera=models.IntegerField()
    precioEconomica=models.IntegerField()
    precioPrimeraDesc=models.IntegerField()
    precioEconomicaDesc=models.IntegerField()

class Compra(models.Model):
    #falta la llave foranea
    precio=models.IntegerField(default=10)
    fecha=models.DateField(auto_now=True)

class Mensaje(models.Model):
    #noticiaid
    #usuariondni
    #respuestaA
    fecha=models.DateField(auto_now=True)

class Noticia(models.Model):
    #usuario id
    fecha=models.DateField(auto_now=True)
    texto=models.CharField(max_length=300)

class Tarjeta(models.Model):
    clienteid=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    tipo=models.CharField(null=False,choices=tipoTarjeta,max_length=16)
    disponible=models.IntegerField(default=200000)
    numero=models.CharField(null=False,max_length=16)
    nombre=models.CharField(null=False,max_length=16)
    cvv=models.CharField(null=False,max_length=3)
    vencimiento=models.DateField()

class Ticket(models.Model):
    Compraid=models.ForeignKey(Compra,on_delete=models.CASCADE,related_name="compraid")
    Vueloid=models.ForeignKey(Vuelo,on_delete=models.CASCADE,related_name="vueloid")
    nombrePasajero=models.CharField(max_length=50,null=False)
    emailPasajero=models.EmailField(null=False)
    edadPasajero=models.IntegerField(null=False)
    asiento=models.CharField(null=False,max_length=4)
    clase=models.CharField(choices=ClaseVuelo,max_length=20)
    EstadoCheckIn=models.CharField(default='No Realizado',max_length=15)



# Create your models here.
