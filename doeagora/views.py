from django.views import generic
from django.urls import reverse_lazy
from . import models

class IndexView(generic.TemplateView):
    template_name = 'doeagora/index.html'

class SobreCadastrosView(generic.TemplateView):
    template_name = 'doeagora/sobrecadastros.html'

class SosDoeInfoView(generic.TemplateView):
    template_name = 'doeagora/sosdoeinfo.html'

class CadastroBeneficiariosView(generic.CreateView):
    template_name = 'doeagora/c.beneficiario.html'
    model = models.Beneficiario
    fields = ("nome", "telefone", "endereco", "cpf", "instituicao")
    success_url = reverse_lazy("doeagora:fim_beneficiados")

class CadastroDoadoresView(generic.CreateView):
    template_name = 'doeagora/c.doadores.html'
    model = models.Doador
    fields = ("nome", "telefone", "email", "endereco", "cpf")
    success_url = reverse_lazy("doeagora:fim_beneficiados")


class CadastroInstituicaoView(generic.CreateView):
    template_name = 'doeagora/c.instituicao.html'
    model = models.Instituicao
    fields = ("nome", "email", "telefone", "endereco" )
    success_url = reverse_lazy("doeagora:fim_beneficiados")
    
    
class DoacoesView(generic.CreateView):
    template_name = 'doeagora/doacao.html'
    model = models.Doacoes
    fields = ("doacao", "quantidade", "data", "instituicao" )
    success_url = reverse_lazy("doeagora:fim_beneficiados")


class FimParaBeneficiadosView(generic.TemplateView):
    template_name = 'doeagora/fim_beneficiados.html'
    

class LoginView(generic.TemplateView):
    template_name = 'doeagora/login.html'
    
 
class VerBeneficiarioView(generic.DetailView):
    template_name = 'doeagora/verbeneficiario.html'
    model = models.Beneficiario
    context_name = 'beneficiario'
    
class VerInstituicaoView(generic.DetailView):
    template_name = 'doeagora/verinstituicao.html'
    model = models.Instituicao
    context_name = 'instituicao'

class VerDoadorView(generic.DetailView):
    template_name = 'doeagora/verdoador.html'
    model = models.Doador
    context_name = 'doador'
