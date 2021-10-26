from django.db import models
from django.contrib.auth.models import User

class Doador(models.Model): 
    nome = models.CharField(max_length=40)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=100, verbose_name="endereço" )
    cpf = models.CharField(max_length=11, verbose_name="CPF")
    email = models.CharField(max_length=40)
       
    class Meta:
        verbose_name = "Doador"
        verbose_name_plural = "Doadores"

    def __str__(self):
        return self.nome
  
class Instituicao(models.Model):
    nome = models.CharField(max_length=40)
    data_ultima_doacao = models.DateField(verbose_name="data da última doação", null=True, blank=True)
    endereco = models.CharField(max_length=100, verbose_name="endereço" )
    email = models.CharField(max_length=40)
    telefone = models.CharField(max_length=11)
   
    class Meta:
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"

    def __str__(self):
        return self.nome
  
  
class Produto(models.Model):
    descricao = models.CharField(max_length=40, verbose_name="descrição")

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.descricao
  

class Beneficiario(models.Model):
    nome = models.CharField(max_length=40)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=100, verbose_name="endereço" )
    cpf = models.CharField(max_length=11, verbose_name="CPF")
    instituicao = models.ForeignKey(Instituicao, verbose_name="instituição", on_delete=models.PROTECT)
 
    class Meta:
        verbose_name = "Beneficiário"
        verbose_name_plural = "Beneficiários"

    def __str__(self):
        return self.nome
 

class Doacao(models.Model):
    quantidade = models.IntegerField()
    data = models.DateField(verbose_name="data da doação", auto_now_add=True)
    doador = models.ForeignKey(Doador, on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.PROTECT)
 
    class Meta:
        verbose_name = "Doação"
        verbose_name_plural = "Doações"
        
class DoacaoBeneficiario(models.Model):
    quantidade = models.IntegerField()
    data = models.DateField(verbose_name="data da doação", auto_now_add=True)
    beneficiario = models.ForeignKey(Beneficiario, on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.PROTECT)
 
    class Meta:
        verbose_name = "Doação para Beneficiario"
        verbose_name_plural = "Doações para Beneficiarios"
    
class Interesse(models.Model):
    quantidade = models.IntegerField()
    data = models.DateField(verbose_name="data da doação", auto_now_add=True)
    beneficiario = models.ForeignKey(Beneficiario, on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Interesse"
        verbose_name_plural = "Interesses"


