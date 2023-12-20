from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True, null=False)
    nome = models.TextField(max_length=200, null=False)
    email = models.EmailField(null=False)
    telefone = models.CharField(max_length=11, null=False)
    