from django.db import models



class Paciente (models.Model): 
    nombre= models.CharField(max_length=40) #str corto
    edad=models.IntegerField() #numero entero
    fecha_nacimiento= models.DateField()

class Crio_Pte (models.Model): 
    estadio_C= models.CharField(max_length=40) #str corto
    cantidad_C=models.IntegerField() #numero entero

class Transfer_Pte (models.Model): 
    estadio_T= models.CharField(max_length=40) #str corto
    cantidad_T=models.IntegerField() #numero entero


