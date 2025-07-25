from django.db import models


class AditivosNutritivos(models.Model):
    data_criacao = models.DateTimeField(blank=True, null=True)
    nome = models.CharField(unique=True, max_length=45)
    formula_quimica = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False # Desabilita a criação da tabela
        db_table = 'aditivos_nutritivos' # Define o nome da tabela


class AditivosNutritivosPicole(models.Model):
    id_picole = models.ForeignKey('Picoles', models.DO_NOTHING, db_column='id_picole', blank=True, null=True)
    id_aditivo_nutritivo = models.ForeignKey(AditivosNutritivos, models.DO_NOTHING, db_column='id_aditivo_nutritivo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aditivos_nutritivos_picole'


class Conservantes(models.Model):
    data_criacao = models.DateTimeField(blank=True, null=True)
    nome = models.CharField(unique=True, max_length=45)
    descricao = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'conservantes'


class ConservantesPicole(models.Model):
    id_picole = models.ForeignKey('Picoles', models.DO_NOTHING, db_column='id_picole', blank=True, null=True)
    id_conservante = models.ForeignKey(Conservantes, models.DO_NOTHING, db_column='id_conservante', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conservantes_picole'


class Ingredientes(models.Model):
    data_criacao = models.DateTimeField(blank=True, null=True)
    nome = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'ingredientes'


class IngredientesPicole(models.Model):
    id_picole = models.ForeignKey('Picoles', models.DO_NOTHING, db_column='id_picole', blank=True, null=True)
    id_ingrediente = models.ForeignKey(Ingredientes, models.DO_NOTHING, db_column='id_ingrediente', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredientes_picole'


class Lotes(models.Model):
    data_criacao = models.DateTimeField(blank=True, null=True)
    quantidade = models.IntegerField()
    id_tipo_picole = models.ForeignKey('TiposPicole', models.DO_NOTHING, db_column='id_tipo_picole')

    class Meta:
        managed = False
        db_table = 'lotes'


class LotesNotaFiscal(models.Model):
    id_nota_fiscal = models.ForeignKey('NotasFiscais', models.DO_NOTHING, db_column='id_nota_fiscal', blank=True, null=True)
    id_lote = models.ForeignKey(Lotes, models.DO_NOTHING, db_column='id_lote', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lotes_nota_fiscal'


class NotasFiscais(models.Model):
    data_criacao = models.DateTimeField(blank=True, null=True)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    numero_serie = models.CharField(unique=True, max_length=45)
    descricao = models.CharField(max_length=200)
    id_revendedor = models.ForeignKey('Revendedores', models.DO_NOTHING, db_column='id_revendedor')

    class Meta:
        managed = False
        db_table = 'notas_fiscais'


class Picoles(models.Model):
    data_criacao = models.DateTimeField(blank=True, null=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    id_sabor = models.ForeignKey('Sabores', models.DO_NOTHING, db_column='id_sabor')
    id_tipo_embalagem = models.ForeignKey('TiposEmbalagem', models.DO_NOTHING, db_column='id_tipo_embalagem')
    id_tipo_picole = models.ForeignKey('TiposPicole', models.DO_NOTHING, db_column='id_tipo_picole')

    class Meta:
        managed = False
        db_table = 'picoles'


class Revendedores(models.Model):
    data_criacao = models.DateTimeField(blank=True, null=True)
    nome = models.CharField(unique=True, max_length=45)
    razao_social = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'revendedores'


class Sabores(models.Model):
    data_criacao = models.DateTimeField(blank=True, null=True)
    nome = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'sabores'


class TiposEmbalagem(models.Model):
    data_criacao = models.DateTimeField(blank=True, null=True)
    nome = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'tipos_embalagem'


class TiposPicole(models.Model):
    data_criacao = models.DateTimeField(blank=True, null=True)
    nome = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'tipos_picole'
