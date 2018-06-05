from django.db import models
from django.utils import timezone


class Home(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=80)
    creada = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(upload_to='uploads/logo')


class Noticias(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=80)
    creada = models.DateTimeField(default=timezone.now)
    publicada = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publicada = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

class Slider(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.TextField(max_length=200)
    imagen = models.ImageField(upload_to='uploads/slider')

    def __str__(self):
        return self.titulo