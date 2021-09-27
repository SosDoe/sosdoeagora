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
    path('ver-beneficiario/<int:pk>', views.VerBeneficiarioView.as_view(), name='ver_beneficiario'),
    path('ver-instituicao/<int:pk>', views.VerInstituicaoView.as_view(), name='ver_instituicao'),
    path('ver-doadores/<int:pk>', views.VerDoadorView.as_view(), name='ver_doador'),
    path('login', views.LoginView.as_view(), name='login'),
    path('doacao', views.DoacaoView.as_view(), name='doacao'),
    path('listagem', views.ListagemView.as_view(), name='listagem'),
    path('listagem-doadores', views.VerListagemDoadorView.as_view(), name='verlistagemdoador'),
    path('listagem-beneficiarios', views.VerListagemBeneficiarioView.as_view(), name='verlistagembeneficiario'),
    path('listagem-instituicoes', views.VerListagemInstituicaoView.as_view(), name='verlistageminstituicao'),
    path('editar-beneficiario/<int:pk>', views.EditarBeneficiarioView.as_view(), name='editar_beneficiario'),
    path('editar-instituicao/<int:pk>', views.EditarInstituicaoView.as_view(), name='editar_instituicao'),
    path('editar-doadores/<int:pk>', views.EditarDoadorView.as_view(), name='editar_doador'),
    path('excluir-beneficiario/<int:pk>', views.ExcluirBeneficiarioView.as_view(), name='excluir_beneficiario'),
    path('excluir-instituicao/<int:pk>', views.ExcluirInstituicaoView.as_view(), name='excluir_instituicao'),
    path('excluir-doadores/<int:pk>', views.ExcluirDoadorView.as_view(), name='excluir_doador'),
    
]
