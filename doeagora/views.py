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
    
class CadastroInteresseView(generic.CreateView):
    template_name = 'doeagora/interesse.html'
    model = models.Interesse
    fields = ("produto", "quantidade", "beneficiario")
    success_url = reverse_lazy("doeagora:index")
   
class CadastroDoacaoBeneficiarioView(generic.CreateView):
    template_name = 'doeagora/d.beneficiario.html'
    model = models.DoacaoBeneficiario
    fields = ("produto", "quantidade", "beneficiario", "instituicao" )
    success_url = reverse_lazy("doeagora:index")

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
    fields = ("quantidade", "doador", "produto", "instituicao" )
    success_url = reverse_lazy("doeagora:fim_beneficiados")


class FimParaBeneficiadosView(generic.TemplateView):
    template_name = 'doeagora/fim_beneficiados.html'
    

class LoginView(generic.TemplateView):
    template_name = 'doeagora/login.html'
    
 
class VerBeneficiarioView(generic.DetailView):
    template_name = 'doeagora/verbeneficiario.html'
    model = models.Beneficiario
    context_name = 'beneficiario'
 
class VerDoacaoView(generic.DetailView):
    template_name = 'doeagora/verdoacao.html'
    model = models.Doacao
    context_name = 'doacao'

class VerInstituicaoView(generic.DetailView):
    template_name = 'doeagora/verinstituicao.html'
    model = models.Instituicao
    context_name = 'instituicao'

class VerDoadorView(generic.DetailView):
    template_name = 'doeagora/verdoador.html'
    model = models.Doador
    context_name = 'doador'
  
class VerInteresseView(generic.DetailView):
    template_name = 'doeagora/verinteresse.html'
    model = models.Interesse
    context_name = 'interesse'
   
class VerDoacaoBeneficiarioView(generic.DetailView):
    template_name = 'doeagora/verinteresse.html'
    model = models.DoacaoBeneficiario
    context_name = 'doacao'

class VerListagemDoacaoView(generic.ListView):
    template_name = 'doeagora/doacao.html'
    model = models.Doacao
    context_object_name = 'doacoes'

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
 
class VerListagemInteresseView(generic.ListView):
    template_name = 'doeagora/verlistageminteresses.html'
    model = models.Interesse
    context_object_name = 'interesses'
   
class VerListagemDoacaoBeneficiarioView(generic.ListView):
    template_name = 'doeagora/verlistagemdoacoesbeneficiarios.html'
    model = models.DoacaoBeneficiario
    context_object_name = 'doacoes'
    
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
  
class EditarInteresseView(generic.UpdateView):
    template_name = 'doeagora/interesse.html'
    model = models.Interesse
    fields = ("produto", "quantidade", "beneficiario")
    success_url = reverse_lazy("doeagora:index")

class EditarDoacaoBeneficiarioView(generic.UpdateView):
    template_name = 'doeagora/c.doadores.html'
    model = models.DoacaoBeneficiario
    fields = ("produto", "quantidade", "beneficiario", "instituicao")
    success_url = reverse_lazy("doeagora:index")

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
 
class ExcluirDoacaoBeneficiarioView(generic.DeleteView):
    template_name = 'doeagora/excluir.html'
    model = models.DoacaoBeneficiario
    success_url = reverse_lazy("doeagora:index")
   
class ExcluirInteresseView(generic.DeleteView):
    template_name = 'doeagora/excluir.html'
    model = models.Interesse
    success_url = reverse_lazy("doeagora:index")
