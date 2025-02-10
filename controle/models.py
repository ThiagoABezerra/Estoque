from django.db import models

class Epi(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    ca = models.CharField(max_length=20)
    estoque = models.IntegerField()   
    tamanho = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    quantidade = models.IntegerField(blank = True,null = True)
    medida = models.IntegerField(blank = True,null = True)
    peso = models.IntegerField(blank = True,null = True)


    def __str__(self):
        return self.name
    
class Departamento(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, related_name='controle_departamento')
    cargo = models.CharField(max_length=200)
    centro_custo = models.IntegerField(blank = True,null = True)

    def __str__(self):
        return self.name