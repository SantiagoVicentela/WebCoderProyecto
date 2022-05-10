from django.db import models
from django.contrib.auth.models import User

class Libro(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=100,verbose_name="Titulo")
    imagen=models.ImageField(upload_to="imagenes/",verbose_name="Imagen",null=True)
    descripcion=models.TextField(verbose_name="Descripcion",null=True)

class Avatar(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     avatar = models.ImageField(upload_to='avatares', null=True, blank=True)



def __str__(self):
        return f'{self.titulo} - {self.descripcion} '
def delete(self, using=None , keep_parents=False):
    self.imagen.storage.delete(self.imagen.name)
    super.delete()
