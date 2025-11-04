from django.contrib import admin
from django.db import models

# Create your models here.

class Livros(models.Model):
    titulo=models.CharField(max_length=100)
    autor =models.CharField(max_length=100)
    ano_de_publicacao=models.IntegerField()
    disponivel = models.BooleanField(default=True)


    def __str__(self):
        return self.titulo


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email =models.EmailField()
    telefone = models.IntegerField()



    def __str__(self):
        return self.nome
    
class Emprestimo(models.Model):
    data_de_emprestimo =models.DateField(auto_now_add=True)
    data_de_devolucao = models.DateField()
    devolvido =models.BooleanField(default=True)
    nome =models.CharField(max_length=100)
    telefone =models.IntegerField()
    email =models.EmailField(null=True)
    usuario =models.ForeignKey(Usuario, on_delete=models.CASCADE)
    livro =models.ForeignKey(Livros, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.usuario} - {self.livro}'

#Permitindo que o administrador faca o cadastro destes 3 componentes    
admin.site.register(Livros)
admin.site.register(Usuario)
admin.site.register(Emprestimo)