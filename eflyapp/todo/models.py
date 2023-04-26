from django.db import models
from .choices import *

class Tarea(models.Model):
    tarea=models.CharField(max_length=100)

    def __str__(self):
        return self.tarea

class Usuario(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    contraseña=models.CharField(max_length=20)
    email=models.EmailField()
    saldo=models.IntegerField(default=0)
    fechaNaci=models.DateField()
    lugarNaci=models.CharField(max_length=50)
    dirFact=models.CharField(max_length=100)
    sexo=models.CharField(max_length=20,choices=genero,default='N')
    tipoUsuario=models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    nombre=models.CharField(max_length=100)
    pais=models.CharField(max_length=100)
    hora=models.TimeField()

    def __str__(self):
        return self.nombre

class Vuelo(models.Model):
    origen=models.ForeignKey(Ciudad,on_delete=models.CASCADE,related_name="origenes")
    destino=models.ForeignKey(Ciudad,on_delete=models.CASCADE,related_name="destinos")
    horaSalida=models.TimeField()
    horaLlegada=models.TimeField()
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
    clienteid=models.ForeignKey(Usuario,on_delete=models.CASCADE,null=True)
    tipo=models.CharField(choices=tipoTarjeta,max_length=20)
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
