from django.db import models
from django.contrib.auth.models import User

class  Categoria(models.Model):
    nome = models.CharField(max_length=65)

    def __str__(self):
        return self.nome

class Panos(models.Model):
    titulo = models.CharField(max_length=65)
    descricao = models.CharField(max_length=165)
    slug = models.SlugField(unique=True)
    preco = models.DecimalField(max_digits=4, decimal_places=2)
    unidade_preco = models.CharField(max_length=10)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    esta_publicado = models.BooleanField(default=False)
    pano_imagem = models.ImageField(upload_to='panos_de_prato/panos_imagens/%d/%m/%Y/', 
                                    blank=True, default='')
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True, blank=True, default=None
    )
    autor = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.titulo
