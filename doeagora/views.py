from django.views import generic
from django.urls import reverse_lazy
from . import models

class IndexView(generic.TemplateView):
    template_name = 'doeagora/index.html'

class SobreCadastrosView(generic.TemplateView):
    template_name = 'doeagora/sobrecadastros.html'

class SosDoeInfoView(generic.TemplateView):
    template_name = 'doeagora/sosdoeinfo.html'

class ListagemView(generic.TemplateView):
    template_name = 'doeagora/listagem.html'

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
    
    
class DoacaoView(generic.CreateView):
    template_name = 'doeagora/doacao.html'
    model = models.Doacao
    fields = ("quantidade", "data", "doador", "produto", "instituicao" )
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
    
class VerListagemBeneficiarioView(generic.ListView):
    template_name = 'doeagora/verlistagembeneficiario.html'
    model = models.Beneficiario
    context_object_name = 'beneficiarios'
    
class VerListagemDoadorView(generic.ListView):
    template_name = 'doeagora/verlistagemdoador.html'
    model = models.Doador
    context_object_name = 'doadores'
    
class VerListagemInstituicaoView(generic.ListView):
    template_name = 'doeagora/verlistageminstituicao.html'
    model = models.Instituicao
    context_object_name = 'instituicoes'
    
class EditarBeneficiarioView(generic.UpdateView):
    template_name = 'doeagora/c.beneficiario.html'
    model = models.Beneficiario
    fields = ("nome", "telefone", "endereco", "cpf", "instituicao")
    success_url = reverse_lazy("doeagora:verlistagembeneficiario")
  
class EditarInstituicaoView(generic.UpdateView):
    template_name = 'doeagora/c.instituicao.html'
    model = models.Instituicao
    fields = ("nome", "email", "telefone", "endereco" )
    success_url = reverse_lazy("doeagora:verlistageminstituicao")
 
class EditarDoadorView(generic.UpdateView):
    template_name = 'doeagora/c.doadores.html'
    model = models.Doador
    fields = ("nome", "telefone", "email", "endereco", "cpf")
    success_url = reverse_lazy("doeagora:verlistagemdoador")

class ExcluirBeneficiarioView(generic.DeleteView):
    template_name = 'doeagora/excluir.html'
    model = models.Beneficiario
    success_url = reverse_lazy("doeagora:verlistagembeneficiario")
  
class ExcluirInstituicaoView(generic.DeleteView):
    template_name = 'doeagora/excluir.html'
    model = models.Instituicao
    success_url = reverse_lazy("doeagora:verlistageminstituicao")
 
class ExcluirDoadorView(generic.DeleteView):
    template_name = 'doeagora/excluir.html'
    model = models.Doador
    success_url = reverse_lazy("doeagora:verlistagemdoador")
