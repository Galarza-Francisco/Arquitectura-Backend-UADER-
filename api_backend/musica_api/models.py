from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=128)
    

    def __str__(self):
        return self.nombre

class Album(models.Model):
    titulo = models.CharField(max_length=128)
    artistas = models.ManyToManyField(Artista, related_name='albums')

    def __str__(self):
        return self.titulo

class Cancion(models.Model):
    titulo = models.CharField(max_length=128)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='canciones')
    artistas = models.ManyToManyField(Artista, related_name='canciones')

    def __str__(self):
        return self.titulo
