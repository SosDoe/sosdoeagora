from django.db import models

class Doador(models.Model): 
  nome = models.CharField(max_length=40)
  telefone = models.CharField(max_length=11)
  endereco = models.CharField(max_length=100, verbose_name="endereço" )
  cpf = models.CharField(max_length=11, verbose_name="CPF")
  
class Instituicao(models.Model):
  desc_benef = models.CharField(max_length=200, verbose_name="descrição do beneficiário")
  nome = models.CharField(max_lenght=40)
  data_ultima_doacao = models.DateField(verbose_name="data da última doação")
  
class Produto(models.Model):
  descricao = models.CharField(max_length=40, verbose_name="descrição")
  

class Beneficiario(models.Model):
  nome = models.CharField(max_length=40)
  telefone = models.CharField(max_length=11)
  endereco = models.CharField(max_length=100, verbose_name="endereço" )
  cpf = models.CharField(max_length=11, verbose_name="CPF")
  instituicao = models.ForeignKey(Instituicao, verbose_name="instituição", on_delete=models.PROTECT)
 

class Doacao(models.Model):
  quantidade = models.IntegerField()
  data_doacao = models.DateField(verbose_name="data da doação")
  doador = models.ForeignKey(Doador, on_delete=models.PROTECT)
  produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
  instituicao = models.ForeignKey(Instituicao, on_delete=models.PROTECT)
  
