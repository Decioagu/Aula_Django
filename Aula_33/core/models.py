from django.db import models


class Filmes(models.Model):
    titulo = models.CharField(primary_key=True, max_length=50)
    genero = models.CharField(max_length=30)
    ano = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'filmes'
