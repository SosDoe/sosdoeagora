from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from myapp.models import BlogPost
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

class Doador(models.Model): 
    nome = models.CharField(max_length=40)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=100, verbose_name="endereço" )
    cpf = models.CharField(max_length=11, verbose_name="CPF")
    email = models.CharField(max_length=40)
    usuario = models.ForeignKey(User, verbose_name="usuário", on_delete=models.PROTECT, null=True)
    user = User.objects.create_user('doador', 'doador@gmail.com', 'doadorpassword')
    user.last_name = 'Doador'
    user.save()

    u = User.objects.get(username='john')
    u.set_password('new password')
    u.save()

    user = authenticate(username='john', password='secret')
    if user is not None:
        # A backend authenticated the credentials
    else:
        # No backend authenticated the credentials
        
    class Meta:
        verbose_name = "Doador"
        verbose_name_plural = "Doadores"
        content_type = ContentType.objects.get_for_model(BlogPost)
        permission = Permission.objects.create(
        codename='can_publish',
        name='Can Publish Posts',
        content_type=content_type,
        )
    
    def __str__(self):
        return self.nome
  
class Instituicao(models.Model):
    nome = models.CharField(max_length=40)
    data_ultima_doacao = models.DateField(verbose_name="data da última doação", null=True, blank=True)
    endereco = models.CharField(max_length=100, verbose_name="endereço" )
    email = models.CharField(max_length=40)
    telefone = models.CharField(max_length=11)
    usuario = models.ForeignKey(User, verbose_name="usuário", on_delete=models.PROTECT, null=True)
    user = User.objects.create_user('doador', 'doador@gmail.com', 'doadorpassword')
    user.last_name = 'Doador'
    user.save()

    u = User.objects.get(username='john')
    u.set_password('new password')
    u.save()

    user = authenticate(username='john', password='secret')
    if user is not None:
        # A backend authenticated the credentials
    else:
        # No backend authenticated the credentials
    
    class Meta:
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"
        content_type = ContentType.objects.get_for_model(BlogPost)
        permission = Permission.objects.create(
        codename='can_publish',
        name='Can Publish Posts',
        content_type=content_type,
        )

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
    usuario = models.ForeignKey(User, verbose_name="usuário", on_delete=models.PROTECT, null=True)
    user = User.objects.create_user('doador', 'doador@gmail.com', 'doadorpassword')
    user.last_name = 'Doador'
    user.save()

    u = User.objects.get(username='john')
    u.set_password('new password')
    u.save()

    user = authenticate(username='john', password='secret')
    if user is not None:
        # A backend authenticated the credentials
    else:
        # No backend authenticated the credentials

    class Meta:
        verbose_name = "Beneficiário"
        verbose_name_plural = "Beneficiários"
        content_type = ContentType.objects.get_for_model(BlogPost)
        permission = Permission.objects.create(
        codename='can_publish',
        name='Can Publish Posts',
        content_type=content_type,
        )

    def __str__(self):
        return self.nome
 

class Doacao(models.Model):
    quantidade = models.IntegerField()
    data = models.DateField(verbose_name="data da doação", auto_now_add=True)
    doador = models.ForeignKey(Doador, on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, verbose_name="usuário", on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = "Doação"
        verbose_name_plural = "Doações"


