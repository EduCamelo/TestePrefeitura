from django.db import models

class Endereco(models.Model):
    link = models.URLField(unique=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.link , self.nome, self.novoLink
