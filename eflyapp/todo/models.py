from django.db import models

class Tarea(models.Model):
    tarea=models.CharField(max_length=100)

    def __str__(self):
        return self.tarea

class Usuarios(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    contraseña=models.CharField(max_length=20)
    email=models.EmailField()
    saldo=models.IntegerField()
    fechaNaci=models.DateField()
    lugarNaci=models.CharField(max_length=50)
    dirFact=models.CharField(max_length=100)
    sexo=models.CharField(max_length=20)
    tipoUsuario=models.CharField(max_length=20)

    def id(self):
        return self.id


class Ciudades(models.Model):
    nombre=models.CharField(max_length=100)
    pais=models.CharField(max_length=100)
    hora=models.TimeField()

    def id(self):
        return self.id

class Vuelos(models.Model):
    origen=models.ForeignKey(Ciudades,on_delete=models.CASCADE,related_name="origenes")
    destino=models.ForeignKey(Ciudades,on_delete=models.CASCADE,related_name="destinos")
    horaSalida=models.TimeField()
    horaLlegada=models.TimeField()
    precioPrimera=models.IntegerField()
    precioEconomica=models.IntegerField()
    precioPrimeraDesc=models.IntegerField()
    precioEconomicaDesc=models.IntegerField()

class Compras(models.Model):
    precio=models.IntegerField(default=10)



# Create your models here.
