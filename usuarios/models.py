from django.db import models

class Nota(models.Model):
    nome_aluno = models.CharField(max_length= 200)
    disciplina = models.CharField(max_length= 200)
    nota_atividades = models.IntegerField(default= 0)
    nota_trabalho = models.FloatField(default= 0)
    nota_prova = models.FloatField(default= 0)
    media = models.FloatField(blank= True, default=0)