from django.urls import path
from . import views

app_name = 'doeagora'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('sobre-cadastros', views.SobreCadastrosView.as_view(), name='sobrecadastros'),
    path('sosdoeinformacoes', views.SosDoeInfoView.as_view(), name='sosdoeinfo'),  
    path('cadastro-beneficiarios', views.CadastroBeneficiariosView.as_view(), name='c.beneficiario'),  
    path('cadastro-doadores', views.CadastroDoadoresView.as_view(), name='c.doadores'),
    path('cadastro-instituicao', views.CadastroInstituicaoView.as_view(), name='c.instituicao'),
    path('fim-cadastro', views.FimParaBeneficiadosView.as_view(), name='fim_beneficiados'),
    path('ver-beneficiario/<int:pk>', views.VerBeneficiarioView.as_view(), name='verbeneficiario'),
    path('ver-instituicao/<int:pk>', views.VerInstituicaoView.as_view(), name='verinstituicao'),
    path('ver-doadores/<int:pk>', views.VerDoadorView.as_view(), name='verdoador'),
    path('login', views.LoginView.as_view(), name='login'),
    path('doacao', views.DoacaoView.as_view(), name='doacao'),
    path('listagem', views.ListagemView.as_view(), name='listagem'),
    path('listagem-doadores', views.VerListagemDoadorView.as_view(), name='verlistagemdoador'),
    path('listagem-beneficiarios', views.VerListagemBeneficiarioView.as_view(), name='verlistagembeneficiario'),
    path('listagem-instituicoes', views.VerListagemInstituicaoView.as_view(), name='verlistageminstituicao'),
]
