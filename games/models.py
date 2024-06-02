from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings


# Create your models here.
#Engranajes
class Engine(models.Model):

    sessionObtained = models.IntegerField(null=True)
    number = models.IntegerField(null=True)


#Perfil
class Profile(models.Model):
    id_de_usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    birth_date = models.DateField(null=True, blank=True)

#Registro
class Games(models.Model):
    avatar= models.ImageField(null=True, blank=True, upload_to='game')
    Game_name = models.CharField(max_length=100, verbose_name="Nombre del juego", null=True, blank=True)
    Game_lang= models.CharField(max_length=100, verbose_name="Lenguaje utilizado", null=True, blank=True)
    Game_engine= models.CharField(max_length=100, verbose_name="Motor")
    Game_description = models.CharField(max_length=500, verbose_name="Descripción del juego")
    Game_dev = models.CharField(max_length=100, verbose_name="Nombre del desarrollador")
    dev_email = models.EmailField(max_length=50, verbose_name="email del desarrollador")
    Game_link = models.URLField(max_length=200, null=True, blank=True, verbose_name="Link del juego")
    created = models.DateField(auto_now_add=True, verbose_name="fecha de creación")

    def __str__(self) -> str:
        return self.Game_name
