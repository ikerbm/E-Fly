from django.db import models
from .choices import *
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime


#Modelo de city-lights
class Address(models.Model):
   country = models.ForeignKey('cities_light.Country', on_delete=models.SET_NULL, null=True, blank=True) 
   city = models.ForeignKey('cities_light.City', on_delete=models.SET_NULL, null=True, blank=True)
   
#Pruebas

class CustomUser(AbstractUser):
    DNI=models.IntegerField(primary_key=True, default=0, validators=[MaxValueValidator(9999999999)])
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
    CIUDADES_PERMITIDAS = [
        ('Pereira', 'Pereira'),
        ('Bogotá', 'Bogotá'),
        ('Medellín', 'Medellín'),
        ('Cali', 'Cali'),
        ('Cartagena', 'Cartagena'),
        ('Madrid', 'Madrid'),
        ('Londres', 'Londres'),
        ('New York', 'New York'),
        ('Buenos Aires', 'Buenos Aires'),
        ('Miami', 'Miami'),
    ]
    codigo = models.CharField(unique=True, null=True, max_length=10)
    origen = models.CharField(max_length=100, choices=CIUDADES_PERMITIDAS)
    destino = models.CharField(max_length=100, choices=CIUDADES_PERMITIDAS)
    filas=models.IntegerField(default=0)
    asientos_fila=models.IntegerField(default=0)
    precioPrimera=models.IntegerField()
    precioEconomica=models.IntegerField()
    precioPrimeraDesc=models.IntegerField(null=True, validators=[MinValueValidator(0)])
    precioEconomicaDesc=models.IntegerField(null=True, validators=[MinValueValidator(0)])
    fechaSalida=models.CharField(null=True, max_length=20)
    horaSalida=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(23)],null=True)
    minutoSalida=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(59)],null=True)
    fechaLlegada=models.CharField(null=True, max_length=20)
    horaLlegada=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(23)],null=True)
    minutoLlegada=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(59)],null=True)
    tiempoVuelo = models.CharField(null=True, max_length=20)

    @property
    def calcular_tiempo_vuelo(self):
        # Realiza el cálculo del tiempo de vuelo
        # utilizando los campos existentes en el modelo
        # y devuelve el resultado en el formato deseado
        # Por ejemplo, vamos a asumir que los campos necesarios son 'hora_salida' y 'hora_llegada'
        if self.fechaLlegada and self.fechaLlegada:
            return self.fechaLlegada  # Formato de ejemplo

        return None  # En caso de que los campos necesarios no estén completos

    def save(self, *args, **kwargs):
        # Antes de guardar el objeto Vuelo, actualizamos el campo calculado 'tiempo_vuelo'
        self.tiempo_vuelo = self.calcular_tiempo_vuelo
        super(Vuelo, self).save(*args, **kwargs)

class Compra(models.Model):
    vuelo=models.ForeignKey(Vuelo,on_delete=models.CASCADE, null=True)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    #falta la llave foranea
    asientos_economica=models.IntegerField(default=10)
    asientos_primera=models.IntegerField(default=10)
    precio=models.IntegerField(default=10)
    fecha=models.DateField(auto_now=True)
    estado=models.CharField(null=True,max_length=16, default='sin_selec')

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

class Seat(models.Model):
    vuelo=models.ForeignKey(Vuelo,on_delete=models.CASCADE, null=True)
    code=models.CharField(null=False,max_length=4)
    estado=models.CharField(null=False,max_length=20)

class Ticket(models.Model):
    Compraid=models.ForeignKey(Compra,on_delete=models.CASCADE,related_name="compraid")
    Vueloid=models.ForeignKey(Vuelo,on_delete=models.CASCADE,related_name="vueloid")
    nombrePasajero=models.CharField(max_length=50,null=True)
    emailPasajero=models.EmailField(null=True)
    edadPasajero=models.IntegerField(null=True)
    asiento=models.ForeignKey(Seat,on_delete=models.CASCADE, null=True)
    clase=models.CharField(choices=ClaseVuelo,max_length=20)
    EstadoCheckIn=models.CharField(default='No Realizado',max_length=15)


# Create your models here.
