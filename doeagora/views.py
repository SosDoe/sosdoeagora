from django.views import generic
from . import models

class IndexView(generic.TemplateView):
    template_name = 'doeagora/index.html'

class SobreCadastrosView(generic.TemplateView):
    template_name = 'doeagora/sobrecadastros.html'

class SosDoeInfoView(generic.TemplateView):
    template_name = 'doeagora/sosdoeinfo.html'

class CadastroBeneficiariosView(generic.TemplateView):
    template_name = 'doeagora/c.beneficiario.html'

class CadastroDoadoresView(generic.TemplateView):
    template_name = 'doeagora/c.doadores.html'

class CadastroInstituicaoView(generic.TemplateView):
    template_name = 'doeagora/c.instituição.html'

class FimParaBeneficiadosView(generic.TemplateView):
    template_name = 'doeagora/fim p beneficiados.html'


