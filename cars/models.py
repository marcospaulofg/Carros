from django.db import models

# Create your models here.

class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Carro(models.Model):
    id = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name='carro_marca')
    ano = models.IntegerField(blank=True, null=True)
    km = models.IntegerField(blank=True, null=True)
    cor = models.CharField(blank=True, null=True, max_length=20)
    preco = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to='carros/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"
    
class Inventario(models.Model):
    id = models.AutoField(primary_key=True)
    quantidade = models.IntegerField()
    valor = models.FloatField()
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data']

    def __str__(self):
        return f"{self.quantidade} - {self.valor}"